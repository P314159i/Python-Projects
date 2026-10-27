import re


class MapParser:
    def __init__(self, path: str) -> None:
        self.path = path
        self.num: int = 0
        self.hub_names: set[str] = set()

        self.start_hub: tuple[str, int, int] | None = None
        self.end_hub: tuple[str, int, int] | None = None

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
            r"(start_hub|end_hub):\s+"
            r"([^\s-]+)\s+(-?\d+)\s+(-?\d+)"
            r"(?:\s+\[([^\]]*)\])?"
        )

        for line_num, line in enumerate(self.lines, 1):
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            if not line.startswith(("start_hub", "end_hub")):
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

            if hub_type == "start_hub" and self.start_hub is not None:
                raise ValueError("Duplicate start hub")

            if hub_type == "end_hub" and self.end_hub is not None:
                raise ValueError("Duplicate end hub")

            if name in self.hub_names:
                raise ValueError(f"Duplicate hub name: {name}")

            self.hub_names.add(name)

            if hub_type == "start_hub":
                self.start_hub = (name, x, y)
            else:
                self.end_hub = (name, x, y)

        if self.start_hub is None:
            raise ValueError("No start hub found")

        if self.end_hub is None:
            raise ValueError("No end hub found")