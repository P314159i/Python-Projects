from src.map_parser import MapParser
from src.parse_rules import Hubs, Connection, Zones
from enum import Enum

class Cost(Enum):
    NORMAL: 



class Graph:
    def __init__(self, parser: MapParser) -> None:
        self.hubs: dict[str, Hubs] = parser.hubs
        self.connections: dict[frozenset[str], Connection] = parser.connections
        self.neighbours: dict[str, dict[str, int]] = {}
        self.cost: dict[Zones, int] = {}

        self.cost = {
            Zones.NORMAL: 1,
            Zones.PRIORITY: 1,
            Zones.RESTRICTED: 2
        }
                
        for name in self.hubs:
            self.neighbours[name] = {}

        for n in self.hubs:
            self.cost[self.hubs[n].zones] = self.cost.Zones

        for connection in self.connections.values():
            a = connection.a
            b = connection.b

            if (self.hubs[a].zone == Zones.BLOCKED
                    or self.hubs[b].zone == Zones.BLOCKED):
                continue

            self.neighbours[a][b] = self.cost[self.hubs[b].zone]
            self.neighbours[b][a] = self.cost[self.hubs[a].zone]

            