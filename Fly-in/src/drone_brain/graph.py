from src.Parsers.map_parser import MapParser
from src.Parsers.parse_rules import Hubs, Connection, Zones

class Graph:

    def __init__(self, parser: MapParser) -> None:
        self.hubs: dict[str, Hubs] = parser.hubs
        self.connections: dict[frozenset[str], Connection] = parser.connections
        self.neighbours: dict[str, dict[str, int]] = {}
        self.cost: dict[Zones, int] = {
            Zones.NORMAL: 1,
            Zones.RESTRICTED: 2,
            Zones.PRIORITY: 1
        }
        for hub in self.hubs:
            self.neighbours[hub] = {} # avoids KeyError later down there

        for con in self.connections.values():
            if self.hubs[con.b].zone != Zones.BLOCKED and self.hubs[con.a].zone != Zones.BLOCKED:
                self.neighbours[con.a][con.b] = self.cost[self.hubs[con.b].zone]
                self.neighbours[con.b][con.a] = self.cost[self.hubs[con.a].zone]

# if __name__ == "__main__":
#     parser = MapParser("./maps/medium/03_priority_puzzle.txt")
#     parser.parse()

#     graph = Graph(parser)
#     print(graph.neighbours)