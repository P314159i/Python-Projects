import re
from .parse_rules import Hubs, Zones, Num, Connection
from pydantic import ValidationError


class MapParser:
    '''Receives and validates a Fly-in map file'''

    def __init__(self, path: str) -> None:
        self.path = path
        self.num: Num | None = None
        self.start_hub: Hubs | None = None
        self.end_hub: Hubs | None = None
        self.hub_name_dup: set[str] = set()
        self.hubs: dict[str, Hubs] = {}
        self.connections: dict[frozenset[str], Connection] = {}
        self.error: list[str] = []
        with open(path, "r") as file:
            self.lines = file.readlines()

    def parse(self) -> None:
        '''Parses the entire map'''

        self._parse_drone()
        self._parse_hubs()
        self._parse_connections()
        print(self.error)

    def _parse_drone(self) -> None:
        '''Reads and validates the drone count'''

        try:

            for line_num, line in enumerate(self.lines, 1):
                line = line.split("#", 1)[0].strip()

                if line in ("nb_drone", "nb_drone:", "nb_drones", "nb_drones:"):
                    raise ValueError(f"[{line_num}] No drone number found")

                if not line:
                    continue

                match = re.fullmatch(r"nb_drones:\s*(.*)", line)

                if match is None:
                    raise ValueError(f"[{line_num}] No nb_drones found")

                try:
                    self.num = int(match.group(1))
                except ValueError:
                    raise ValueError(f"[{line_num}] Invalid drone number")

                if self.num < 0:
                    raise ValueError(f"[{line_num}] Drone count must be positive")

                if self.num == 0:
                    raise ValueError(f"[{line_num}] Drone count must be non-Zero")

                self.num = int(match.group(1))
                if self.num:
                    break

            for n, later_line in enumerate(self.lines[line_num:], line_num + 1):
                later_line = later_line.split("#", 1)[0].strip()

                if later_line.startswith("nb_drones"):
                    raise ValueError(
                        f"[{n}: {later_line}] Duplicate drone count"
                    )

        except ValueError as err:
            raise

        return self.num

    def _parse_hubs(self) -> None:
        '''Read and validate hub definitions.'''

        pattern = re.compile( # repeated use
            r"(start_hub|end_hub|hub):\s+"
            r"([^\s-]+)\s+(-?\d+)\s+(-?\d+)"
            r"(?:\s+\[([^\[\]]+)\])?"
        )

        for line_num, line in enumerate(self.lines, 1):
            line = line.split("#", 1)[0].strip()

            if not line or not line.startswith(("start_hub", "end_hub", "hub")):
                continue

            match = pattern.fullmatch(line)

            if match is None:
                raise ValueError(
                    f"[{line_num}: {line}] Invalid hub definition"
                )

            hub_type = match.group(1)
            name = match.group(2)
            x = int(match.group(3))
            y = int(match.group(4))

            metadata: dict[str, str] = {}

            for item in (match.group(5) or "").split():
                pair = re.fullmatch(r"(zone|color|max_drones)=([^=]+)", item)

                if pair is None or pair.group(1) in metadata:
                    raise ValueError(
                        f"[{line_num}: {line}] Invalid metadata"
                    )

                metadata[pair.group(1)] = pair.group(2)

            try:
                zone = Zones(metadata.get("zone", "normal"))
                max_drones = 1

                if hub_type == "hub":
                    max_drones = int(metadata.get("max_drones", "1"))

            except ValueError:
                raise ValueError(f"[{line_num}]: Invalid metadata")

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
                raise ValueError(f"[{line_num}]: Max_drone should be greater or equal to 1")

            if hub_type == "start_hub" and self.start_hub is not None:
                raise ValueError(
                    f"[{line_num}: {line}] Duplicate start hub"
                )

            if hub_type == "end_hub" and self.end_hub is not None:
                raise ValueError(
                    f"[{line_num}: {line}] Duplicate end hub"
                )

            if name in self.hub_name_dup:
                raise ValueError(
                    f"[{line_num}: {line}] Duplicate hub name: {name}"
                )

            self.hub_name_dup.add(name)
            self.hubs[name] = hub

            if hub_type == "start_hub":
                self.start_hub = hub

            if hub_type == "end_hub":
                self.end_hub = hub

        if self.start_hub is None:
            raise ValueError(
                f"[{len(self.lines) + 1}] No start hub found"
            )

        if self.end_hub is None:
            raise ValueError(
                f"[{len(self.lines) + 1}] No end hub found"
            )

    def _parse_connections(self) -> None:
        """Read and validate connections."""

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
                raise ValueError(
                    f"[{line_num}: {line}] Invalid connection syntax"
                )

            a, b = match.group(1), match.group(2)

            if a not in self.hubs or b not in self.hubs:
                raise ValueError(
                    f"[{line_num}: {line}] Undefined connection hub"
                )

            try:
                capacity = int(match.group(3)) if match.group(3) is not None else 1
                connection = Connection(
                    a=a, b=b, max_link_capacity=capacity
                )
            except (ValueError, ValidationError):
                raise ValueError(
                    f"[{line_num}: {line}] Invalid connection capacity"
                ) from None

            edge = frozenset((a, b))

            if edge in self.connections:
                raise ValueError(
                    f"[{line_num}: {line}] Duplicate connection"
                )

            self.connections[edge] = connection


x = MapParser("./maps/medium/03_priority_puzzle.txt")
try:
    x.parse()
except ValueError as err:
    print(f"Error: {err}")
    raise SystemExit(1)
