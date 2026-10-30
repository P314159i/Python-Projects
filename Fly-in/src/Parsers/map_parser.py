import re
from .parse_rules import Hubs, Num, Zones


class MapParser:
    def __init__(self, path: str) -> None:
        self.path = path
        self.num: Num | None = 0
        self.start_hub: Hubs | None = None
        self.end_hub: Hubs | None = None
        self.hub_name_dup: set[str] = set()
        self.hubs: dict[str, Hubs] = {}
        self.connections: dict[frozenset[str], int] = {}

        with open(path, "r") as file:
            self.lines = file.readlines()

    def parse_drone(self) -> None:
        for line_num, line in enumerate(self.lines, 1):
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            match = re.fullmatch(r"nb_drones:\s*(.*)", line)

            if match is None:
                raise ValueError(
                    f"Line {line_num}: No drone count on first line"
                )

            try:
                self.num = int(match.group(1))
            except ValueError:
                raise ValueError(
                    f"Line {line_num}: Invalid drone number"
                )

            if self.num <= 0:
                raise ValueError(
                    f"Line {line_num}: Drone count must be positive"
                )

            return

        raise ValueError("No drone count found")

    def parse_hub(self) -> None:
        pattern = re.compile(
            r"(start_hub|end_hub|hub):\s+"
            r"([^\s-]+)\s+(-?\d+)\s+(-?\d+)"
            r"(?:\s+\[([^\]]*)\])?"
        )

        for line_num, line in enumerate(self.lines, 1):
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            if not line.startswith(("start_hub", "end_hub", "hub")):
                continue

            match = pattern.fullmatch(line)

            if match is None:
                raise ValueError(
                    f"Line {line_num}: Invalid hub definition"
                )

            hub_type = match.group(1)
            name = match.group(2)
            x = int(match.group(3))
            y = int(match.group(4))

            z = re.search(r"\bzone=(\w+)", match.group(5) or "")
            zone = Zones(z.group(1)) if z else Zones.NORMAL

            c = re.search(r"\bcolor=(\w+)", match.group(5) or "")
            color = c.group(1) if c else None

            m = re.search(r"\bmax_drones=(\w+)", match.group(5) or "")
            max_drones = int(m.group(1)) if m else 1

            hub = Hubs(
                name=name, x=x, y=y,
                zone=zone, color=color,
                max_drones=max_drones
            )

            if hub_type == "start_hub" and self.start_hub is not None:
                raise ValueError("Duplicate start hub")

            if hub_type == "end_hub" and self.end_hub is not None:
                raise ValueError("Duplicate end hub")

            if name in self.hub_name_dup:
                raise ValueError(f"Duplicate hub name: {name}")

            self.hub_name_dup.add(name)

            self.hubs[name] = hub

            if hub_type == "start_hub":
                self.start_hub = hub

            if hub_type == "end_hub":
                self.end_hub = hub

        if self.start_hub is None:
            raise ValueError("No start hub found")

        if self.end_hub is None:
            raise ValueError("No end hub found")

    def parse_connections(self) -> None:
        '''connections have hub-hub as name'''

        defined_hubs: set[str] = set()

        for line_num, line in enumerate(self.lines, 1):
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            if line.startswith(("hub:", "start_hub:", "end_hub:")):
                defined_hubs.add(line.split()[1])
                continue

            if not line.startswith("connection:"):
                continue

            match = re.fullmatch(
                r"connection:\s+([^\s-]+)-([^\s-]+)"
                r"(?:\s+\[max_link_capacity=(\d+)\])?",
                line
            )

            if match is None:
                raise ValueError(
                    f"Line {line_num}: Invalid connection"
                )

            a, b = match.group(1), match.group(2)
            capacity = int(match.group(3) or 1)

            if a not in defined_hubs or b not in defined_hubs:
                raise ValueError(
                    f"Line {line_num}: Undefined hub"
                )

            if capacity < 1:
                raise ValueError(
                    f"Line {line_num}: Invalid link capacity"
                )

            edge = frozenset((a, b))

            if edge in self.connections:
                raise ValueError(
                    f"Line {line_num}: Duplicate connection"
                )

            self.connections[edge] = capacity