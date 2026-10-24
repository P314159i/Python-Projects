import re


class MapParser:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.num: int = 0
        self.shub: tuple[int, int] | None = None
        self.ehub: tuple[int, int] | None = None

        with open(self.file_path, "r") as file:
            self.lines: list[str] = file.readlines()

    def parse(self) -> tuple[int, tuple[int, int], tuple[int, int]]:
        found_drone = False

        for line_no, l in enumerate(self.lines, start=1):
            l = l.strip()

            # Ignore comments and empty lines
            if not l or l.startswith("#"):
                continue

            # FIRST: Drone count
            if not found_drone:
                match = re.fullmatch(r"nb_drones:\s*(.*)", l)

                if not match:
                    raise ValueError(f"Line {line_no}: Missing nb_drones")

                value = match.group(1).strip()

                if not value:
                    raise ValueError(f"Line {line_no}: Empty drone count")

                try:
                    self.num = int(value)
                except ValueError:
                    raise ValueError(
                        f"Line {line_no}: Invalid drone number"
                    ) from None

                if self.num <= 0:
                    raise ValueError(f"Line {line_no}: Invalid drone count")

                found_drone = True
                continue

            # SECOND: Start and end hubs
            if l.startswith(("start_hub:", "end_hub:")):

                match = re.fullmatch(
                    r"(start_hub|end_hub):\s+"
                    r"([^\s-]+)\s+"
                    r"(-?\d+)\s+(-?\d+)"
                    r"(?:\s+\[([^\]]*)\])?",
                    l
                )

                if not match:
                    raise ValueError(f"Line {line_no}: Invalid hub format")

                kind = match.group(1)
                name = match.group(2)
                x = int(match.group(3))
                y = int(match.group(4))

                if kind == "start_hub":
                    if self.shub is not None:
                        raise ValueError(f"Line {line_no}: Duplicate start")
                    self.shub = (x, y)

                elif kind == "end_hub":
                    if self.ehub is not None:
                        raise ValueError(f"Line {line_no}: Duplicate end")
                    self.ehub = (x, y)

        if not found_drone or self.shub is None or self.ehub is None:
            raise ValueError("Missing required drone count or hubs")

        return self.num, self.shub, self.ehub


if __name__ == "__main__":
    try:
        x = MapParser("maps/hard/02_capacity_hell.txt")
        print(x.parse())
    except (ValueError, OSError) as err:
        print(err)
