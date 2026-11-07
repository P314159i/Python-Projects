from src.Parsers.map_parser import MapParser
from src.Parsers.parse_rules import Hubs, Connection, Zones


class Graph:
    def __init__(self, parser: MapParser) -> None:
        ''' The kaas between dijkstra and parser sandwitch '''

        self.hubs: dict[str, Hubs] = parser.hubs
        self.neighbours: dict[str, dict[str, int]] = {}
        self.connections: dict[frozenset[str], Connection] = parser.connections
        self.cost: dict[Zones, int] = {
            Zones.NORMAL: 1,
            Zones.PRIORITY: 1,
            Zones.RESTRICTED: 2
        }


        for name in self.hubs:
            self.neighbours[name] = {}

        for connection in self.connections.values():
            a = connection.a
            b = connection.b

            if (self.hubs[a].zone == Zones.BLOCKED
                    or self.hubs[b].zone == Zones.BLOCKED):
                continue

            self.neighbours[a][b] = self.cost[self.hubs[b].zone]
            self.neighbours[b][a] = self.cost[self.hubs[a].zone]


# if __name__ == "__main__":
#     parser = MapParser("./maps/medium/03_priority_puzzle.txt")
#     parser.parse()

#     graph = Graph(parser)
#     print(graph.neighbours)