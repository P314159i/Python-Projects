
import re
from pydantic import ValidationError
from .parse_rules import Hubs, Zones, Num, Connection


class MapParser:
    '''Receives and validates a Fly-in map file.'''

    def __init__(self, path: str) -> None:
        self.path = path
        self.num: Num | None = None
        self.start_hub: Hubs | None = None
        self.end_hub: Hubs | None = None
        self.hub_name_dup: set[str] = set()
        self.hubs: dict[str, Hubs] = {}
        self.hub_lines: dict[str, int] = {}
        self.connections: dict[frozenset[str], Connection] = {}
        self.error: list[tuple[str, str]] = []
        self._parsed = False

        with open(path, "r") as file:
            self.lines = file.readlines()

    def parse(self) -> None:
        '''Parses the entire map.'''

        if self._parsed:
            return
        self._parsed = True
        self._parse_drone()
        self._parse_hubs()
        self._parse_connections()
        self._check_unknown_lines()

        if self.error:
            messages = "\n".join(
                f"{kind}: {message}"
                for kind, message in self.error
            )
            raise ValueError(messages)

    def _parse_drone(self) -> None:
        '''Reads and validates the drone count.'''

        first_line_num: int | None = None

        for line_num, line in enumerate(self.lines, 1):
            line = line.split("#", 1)[0].strip()

            if not line:
                continue

            first_line_num = line_num

            if line in ("nb_drone", "nb_drone:", "nb_drones", "nb_drones:"):
                self.error.append((
                    "ValueError",
                    f"[{line_num}] No drone number found"
                ))
            else:
                match = re.fullmatch(r"nb_drones:\s*(.*)", line)

                if match is None:
                    self.error.append((
                        "ValueError",
                        f"[{line_num}] No nb_drones found"
                    ))
                elif not match.group(1).strip():
                    self.error.append((
                        "ValueError",
                        f"[{line_num}] No drone number found"
                    ))
                else:
                    try:
                        number = int(match.group(1))
                    except ValueError:
                        self.error.append((
                            "ValueError",
                            f"[{line_num}] Invalid drone number"
                        ))
                    else:
                        try:
                            self.num = Num(num=number)
                        except ValidationError as err:
                            for issue in err.errors():
                                self.error.append((
                                    "ValidationError",
                                    f"[{line_num}] "
                                    f"{issue['loc']}: {issue['msg']}"
                                ))
            break

        if first_line_num is None:
            self.error.append((
                "ValueError", "[1] No drone count found"
            ))
            return

        for n, later_line in enumerate(
            self.lines[first_line_num:], first_line_num + 1
        ):
            later_line = later_line.split("#", 1)[0].strip()

            if later_line.startswith("nb_drones"):
                self.error.append((
                    "ValueError",
                    f"[{n}: {later_line}] Duplicate drone count"
                ))

    def _parse_hubs(self) -> None:
        '''Read and validate hub definitions.'''

        pattern = re.compile(
            r"(start_hub|end_hub|hub):\s+"
            r"([^\s-]+)\s+(-?\d+)\s+(-?\d+)"
            r"(?:\s+\[([^\[\]]+)\])?"
        )

        for line_num, line in enumerate(self.lines, 1):
            line = line.split("#", 1)[0].strip()

            if not line or not line.startswith(
                ("start_hub", "end_hub", "hub")
            ):
                continue

            match = pattern.fullmatch(line)

            if match is None:
                self.error.append((
                    "ValueError",
                    f"[{line_num}: {line}] Invalid hub definition"
                ))
                continue

            hub_type = match.group(1)
            name = match.group(2)
            x = int(match.group(3))
            y = int(match.group(4))

            metadata: dict[str, str] = {}
            invalid_metadata = False

            for item in (match.group(5) or "").split():
                pair = re.fullmatch(
                    r"(zone|color|max_drones)=([^=]+)", item
                )

                if pair is None or pair.group(1) in metadata:
                    self.error.append((
                        "ValueError",
                        f"[{line_num}: {line}] Invalid metadata"
                    ))
                    invalid_metadata = True
                    break

                metadata[pair.group(1)] = pair.group(2)

            if invalid_metadata:
                continue

            try:
                zone = Zones(metadata.get("zone", "normal"))
                max_drones = 1

                if hub_type == "hub":
                    max_drones = int(metadata.get("max_drones", "1"))

            except ValueError:
                self.error.append((
                    "ValueError",
                    f"[{line_num}] Invalid metadata"
                ))
                continue

            color = metadata.get("color")

            try:
                hub = Hubs(
                    name=name,
                    x=x,
                    y=y,
                    zone=zone,
                    color=color,
                    max_drones=max_drones
                )
            except ValidationError as err:
                for issue in err.errors():
                    self.error.append((
                        "ValidationError",
                        f"[{line_num}] "
                        f"{issue['loc']}: {issue['msg']}"
                    ))
                continue

            if hub_type == "start_hub" and self.start_hub is not None:
                self.error.append((
                    "ValueError",
                    f"[{line_num}: {line}] Duplicate start hub"
                ))
                continue

            if hub_type == "end_hub" and self.end_hub is not None:
                self.error.append((
                    "ValueError",
                    f"[{line_num}: {line}] Duplicate end hub"
                ))
                continue

            if name in self.hub_name_dup:
                self.error.append((
                    "ValueError",
                    f"[{line_num}: {line}] Duplicate hub name: {name}"
                ))
                continue

            self.hub_name_dup.add(name)
            self.hubs[name] = hub
            self.hub_lines[name] = line_num

            if hub_type == "start_hub":
                self.start_hub = hub

            if hub_type == "end_hub":
                self.end_hub = hub

        if self.start_hub is None:
            self.error.append((
                "ValueError",
                f"[{len(self.lines) + 1}] No start hub found"
            ))

        if self.end_hub is None:
            self.error.append((
                "ValueError",
                f"[{len(self.lines) + 1}] No end hub found"
            ))

    def _parse_connections(self) -> None:
        '''Read and validate connections.'''

        for line_num, line in enumerate(self.lines, 1):
            line = line.split("#", 1)[0].strip()

            if not line.startswith("connection:"):
                continue

            match = re.fullmatch(
                r"connection:\s+([^\s-]+)-([^\s-]+)"
                r"(?:\s+\[max_link_capacity=([^\]]*)\])?",
                line
            )

            if match is None:
                self.error.append((
                    "ValueError",
                    f"[{line_num}: {line}] Invalid connection syntax"
                ))
                continue

            a, b = match.group(1), match.group(2)

            if a not in self.hubs or b not in self.hubs:
                self.error.append((
                    "ValueError",
                    f"[{line_num}: {line}] Undefined connection hub"
                ))
                continue

            if (
                self.hub_lines[a] >= line_num
                or self.hub_lines[b] >= line_num
            ):
                self.error.append((
                    "ValueError",
                    f"[{line_num}: {line}] "
                    "Connection hub defined too late"
                ))
                continue

            try:
                capacity = (
                    int(match.group(3))
                    if match.group(3) is not None else 1
                )
            except ValueError:
                self.error.append((
                    "ValueError",
                    f"[{line_num}: {line}] Invalid connection capacity"
                ))
                continue

            try:
                connection = Connection(
                    a=a,
                    b=b,
                    max_link_capacity=capacity
                )
            except ValidationError as err:
                for issue in err.errors():
                    self.error.append((
                        "ValidationError",
                        f"[{line_num}] "
                        f"{issue['loc']}: {issue['msg']}"
                    ))
                continue

            edge = frozenset((a, b))

            if edge in self.connections:
                self.error.append((
                    "ValueError",
                    f"[{line_num}: {line}] Duplicate connection"
                ))
                continue

            self.connections[edge] = connection

    def _check_unknown_lines(self) -> None:
        valid_prefixes = (
            "nb_drones:",
            "start_hub:",
            "end_hub:",
            "hub:",
            "connection:"
        )

        first_seen = False

        for line_num, line in enumerate(self.lines, 1):
            line = line.split("#", 1)[0].strip()

            if not line:
                continue

            if not first_seen:
                first_seen = True
                continue

            if line.startswith("nb_drones"):
                continue

            if not line.startswith(valid_prefixes):
                self.error.append((
                    "ValueError",
                    f"[{line_num}: {line}] Unknown line"
                ))


# if __name__ == "__main__":
#     x = MapParser("./maps/medium/03_priority_puzzle.txt")

#     try:
#         x.parse()
#     except ValueError as err:
#         print(f"Error: {err}")
#         raise SystemExit(1)
