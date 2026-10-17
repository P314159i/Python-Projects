class MapParser:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.num: int = 0
        with open(self.file_path, "r") as file:
            self.lines: list[str] = file.readlines()
    
    def drone_count(self) -> int:
        flag = 0
        for line_no, l in enumerate(self.lines, start=1):
            if not l.startswith("#") and l.strip():
                i = l.find("nb_drones: ")
                if i != -1:
                    flag = 1
                    try:
                        self.num = int(l[i + len("nb_drones: "):].strip())
                        if self.num <= 0:
                            print(f"Hault! Invalid drone number at line {line_no}!")
                            return 0
                        if l[i + len("nb_drones: "):].strip() = "":
                            print(f"Hault! No drone number at line {line_no}!")
                            return 0
                    except ValueError as err:
                        print(f"Hault! Invalid drone number at line {line_no}!")
                        return 0
        if flag == 0:
            print("Hault! There is no drone mentioned")
            return 0
            
        print(self.num)
        return self.num



if __name__ == "__main__":
    x = MapParser("maps/hard/02_capacity_hell.txt")
    # print(x.lines)
    # print(x.lines[0])
    # print(x.drone_num())
    x.drone_count()