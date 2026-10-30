import re
from .parse_rules import Hubs, Zones


class MapParser:
    """Read and validate a Fly-in map file."""

    def __init__(self, path: str) -> None:
        self.path = path
        self.num: int | None = None
        self.start_hub: Hubs | None = None
        self.end_hub: Hubs | None = None
        self.hub_name_dup: set[str] = set()
        self.hubs: dict[str, Hubs] = {}
        self.connections: dict[frozenset[str], int] = {}

        with open(path, "r") as file:
            self.lines = file.readlines()

    def parse(self) -> None:
        """Parse the entire map."""
        self.parse_drone()
        self.parse_hub()
        self.parse_connections()

    def parse_drone(self) -> None:
        """Read and validate the drone count."""
        for line_num, line in enumerate(self.lines, 1):
            line = line.split("#", 1)[0].strip()

            if not line:
                continue

            match = re.fullmatch(r"nb_drones:\s*(.*)", line)

            if match is None:
                raise ValueError(
                    f"[{line_num}: {line}] No drone count on first line"
                )

            try:
                number = int(match.group(1))
            except ValueError:
                raise ValueError(
                    f"[{line_num}: {line}] Invalid drone number"
                )

            if number <= 0:
                raise ValueError(
                    f"[{line_num}: {line}] Drone count must be positive"
                )

            self.num = number

            for n, later_line in enumerate(self.lines[line_num:], line_num + 1):
                later_line = later_line.split("#", 1)[0].strip()

                if later_line.startswith("nb_drones"):
                    raise ValueError(
                        f"[{n}: {later_line}] Duplicate drone count"
                    )
            return

        raise ValueError("[1] No drone count found")

    def parse_hub(self) -> None:
        """Read and validate hub definitions."""
        pattern = re.compile(
            r"(start_hub|end_hub|hub):\s+"
            r"([^\s-]+)\s+(-?\d+)\s+(-?\d+)"
            r"(?:\s+\[([^\[\]]+)\])?"
        )

        for line_num, line in enumerate(self.lines, 1):
            line = line.split("#", 1)[0].strip()

            if not line:
                continue

            if not line.startswith(("start_hub", "end_hub", "hub")):
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
            except ValueError as err:
                raise ValueError(f"[{line_num}]: {err}")

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

    def parse_connections(self) -> None:
        """Read and validate connections."""
        defined_hubs: set[str] = set()

        for line_num, line in enumerate(self.lines, 1):
            line = line.split("#", 1)[0].strip()

            if not line:
                continue

            if line.startswith(("hub:", "start_hub:", "end_hub:")):
                defined_hubs.add(line.split()[1])
                continue

            if line.startswith("nb_drones:"):
                continue

            if not line.startswith("connection:"):
                raise ValueError(
                    f"[{line_num}: {line}] Unknown line"
                )

            match = re.fullmatch(
                r"connection:\s+([^\s-]+)-([^\s-]+)"
                r"(?:\s+\[max_link_capacity=(\d+)\])?",
                line
            )

            if match is None:
                raise ValueError(
                    f"[{line_num}: {line}] Invalid connection"
                )

            a, b = match.group(1), match.group(2)
            capacity = int(match.group(3) or 1)

            if a not in defined_hubs or b not in defined_hubs:
                raise ValueError(
                    f"[{line_num}: {line}] Undefined hub in connection"
                )

            if capacity < 1:
                raise ValueError(
                    f"[{line_num}: {line}] Invalid link capacity"
                )

            edge = frozenset((a, b))

            if edge in self.connections:
                raise ValueError(
                    f"[{line_num}: {line}] Duplicate connection"
                )

            self.connections[edge] = capacity
