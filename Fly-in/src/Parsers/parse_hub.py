import re


class HubParser:
    def __init__(self, path: str) -> None:
        self.path = path
        with open(path, "r") as file:
            self.lines = file.readlines()

    def parse_hub(self) -> None:
            flag_start_found = 0
            flag_end_found = 0
            hub_names: set = set()

            try:
                for l in self.lines:
                    l = l.strip()

                    if l.startswith("#") or l == "":
                        continue

                    match_obj_s = re.fullmatch(
                        r"start_hub:\s+(\S+)\s+(-?\d+)\s+(-?\d+)(?:\s+\[([^\]]*)\])?",
                        l)

                    match_obj_e = re.fullmatch(
                        r"end_hub:\s+(\S+)\s+(-?\d+)\s+(-?\d+)(?:\s+\[([^\]]*)\])?",
                        l)

                    if match_obj_s is not None:
                        if flag_start_found == 1:
                            raise ValueError("Duplicate start hubs!")
                        else:
                            if  match_obj_s.group(1) not in hub_names:
                                hub_names.add(match_obj_s.group(1))
                            else:
                                raise ValueError("Your start hub name is not as unique as you think")

                            try:
                                start_hub_coordinate: tuple[int, int] = (
                                    int(match_obj_s.group(2)),
                                    int(match_obj_s.group(3))
                                )
                                flag_start_found = 1
                            except ValueError as err:
                                print("Invalid hub coordinates")

                    if match_obj_e is not None:
                        if flag_end_found == 1:
                            raise ValueError("Duplicate end hub!")
                        else:
                            if  match_obj_e.group(1) not in hub_names:
                                hub_names.add(match_obj_e.group(1))
                            else:
                                raise ValueError("Your end hub name is not as unique as you think")

                            try:
                                end_hub_coordinate: tuple[int, int] = (
                                    int(match_obj_e.group(2)),
                                    int(match_obj_e.group(3))
                                )
                                flag_end_found = 1

                            except ValueError as err:
                                print("Invalid hub coordinates")

                if flag_end_found == 0:
                    raise ValueError("No end hub found")
                if flag_start_found == 0:
                    raise ValueError("No start hub found")

                # print(end_hub_coordinate, start_hub_coordinate, self.num)

            except ValueError as err:
                print(err)


Names: No spaces or hyphens; no duplicate names.
Metadata: Optional, but must use valid key=value syntax.
Zone: Only normal, blocked, restricted, or priority.
Color: Any single word.
Capacity: max_drones is ignored for start and end hubs.
Malformed lines: Reject invalid hub definitions instead of silently skipping them

Regex → Extract hub name, coordinates, and metadata.
Dictionary → Convert metadata like zone=priority color=red into key-value pairs.
Pydantic BaseModel → Define the hub fields.
Field → Enforce rules like positive capacities.
Literal → Restrict zones to the four allowed values.
field_validator → Handle custom validation rules.
