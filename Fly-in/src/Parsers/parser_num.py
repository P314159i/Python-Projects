import re


class NumParser:
    def __init__(self, path: str) -> None:
        self.path = path
        self.num: int = 0
        with open(path, "r") as file:
            self.lines = file.readlines()

    def parse_drone(self) -> None:
        found_num_flag = 0
        try:
            for l in self.lines:
                l = l.strip()

                if l.startswith("#") or l == "":
                    continue

                match_obj = re.fullmatch(r"nb_drones:\s*(.*)", l)

                if match_obj is None:
                    raise ValueError("No drone count on first line")

                try:
                    self.num = int(match_obj.group(1))
                    if self.num > 0:
                        found_num_flag = 1
                        break

                except ValueError:
                    raise ValueError("Invalid drone number")

                if self.num < 0:
                    raise ValueError(
                        "How can you drive negative number of drones?"
                    )

                if self.num == 0:
                    raise ValueError("You have no drones bro")

        except ValueError as err:
            print(err)
        
    

if __name__ == "__main__":
    x = MapParser("maps/challenger/01_the_impossible_dream.txt") # remove and make a flyin or main.py
    x.parse_drone()
    x.parse_hub()



# .group(0) → the entire matched text: "nb_drones: 25"
# .group(1) → text captured by the first parentheses (.*): "25"
# .group(2) → text captured by the second pair of parentheses, if present.

# to avoid traceback:
# try:
#     raise ValueError("blahlhalh")
# except ValueError as err:
#     print(err)