class MapParser:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.num: int = 0
        self.shub: tuple[int, int]
        self.ehub: tuple[int, int]
        self.line_no = 0
        self.flag_found_drone = 0
        with open(self.file_path, "r") as file:
            self.lines: list[str] = file.readlines()

    def parse(self) -> int, tuple[int, int], tuple[int, int]:
        for self.line_no, l in enumerate(self.lines, start=1):
            if not l.startswith("#") and l.strip():
                if l.find("nb_drones: ") != -1:
                    try:
                        d = l.find("nb_drones: ")
                        if l[d + len("nb_drones: "):].strip() == "":
                            print(f"Hault! No drone number specified (line {self.line_no})")
                            return 0
                        self.num = int(l[d + len("nb_drones: "):].strip())
                        if self.num <= 0:
                            print(f"Hault! drone number is negative/zero (line {self.line_no})")
                            return 0
                        self.flag_found_drone = 1
                    except ValueError as err:
                        print(f"Hault! drone number is not a digit (line {self.line_no})")
                        return 0
                    break
                else:
                    print("No drone found in the first line")
                    return 0
        for self.line_no, l in enumerate(
            self.lines[self.line_no:], start=self.line_no + 1
            ):
            if self.flag_found_drone == 1:
                if l.find("start_hub: ") != -1:
                    try:
                        s = l.find("start_hub: ")
                        if l[s + len("start_hub: start "):].strip() == "":
                            print(f"Hault! No start hub specified (line {self.line_no})")
                            return 0
                        string = l[d + len("start_hub: start "):].strip()
                        try:
                            self.shub = l.split("[", 1)[0]

            

        print(f"line number for drone: {self.line_no}")
        print(f"drone number: {self.num}")
        return self.num, self.shub, self.ehub




if __name__ == "__main__":
    x = MapParser("maps/hard/02_capacity_hell.txt")
    # print(x.lines)
    # print(x.lines[0])
    # print(x.drone_num())
    x.parse()
