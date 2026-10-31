import re
from .parse_rules import Hubs, Zones

class MapParser:
    def __init__(self, path: str) -> None:
        self.path = path
        self.num: int | None = None
        self.hubs: dict [str, Hubs] | None = None
        self.start_hub: Hubs | None = None
        self.end_hub: Hubs | None = None
        self.hub_name_dub: set[str] = set()
        self.zone: Zones | None = None
        self.connections: dict[frozenset[str], int | None] = {}
        with open(path, "r") as file:
            self_lines = file.readlines()

        def parser(self) -> None:
            self.parse_drone()
            self.parse_hub()
            self.parse_connections()

        def parse_hub(self) -> None:

            for line_num, line in enumerate(self.lines, 1):
                line = line.split