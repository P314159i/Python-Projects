from src.Parsers.map_parser import MapParser
from .simul_rules import Drone
from pathlib import Path
from src.drone_brain.graph import Graph
from src.drone_brain.dijkstra import dijkstra, path_maker


def _drone_constructor(
    num_drones: int, start: str, end: str, path: list[str]
    ) -> list[Drone]:

    if not path:
        raise ValueError("No path from start to end found by the algorithm")

    drones: list[Drone] = []
    for i in range(num_drones):
        drone = Drone(
            name=f"donr_{i}",
            current_hub=start,
            path=path.copy()
        )
        drones.append(drone)

    return drones


def drone_trafficing(map_path: Path) -> None:

    parser = MapParser(map_path)
    parser.parse()
    graph = Graph(parser)
    start = parser.start_hub.name
    end = parser.end_hub.name
    hub_occupied: dict[str, int] = {}
    link_occupied: dict[frozenset[str], int] = {}
    _, next_hop = dijkstra(graph, end)
    path = path_maker(start, end, next_hop)
    drones = _drone_constructor(parser.num.num, start, end, path) #Num>num

    for p in path:
        hub_occupied[p] = 0
        hub_occupied[start] = parser.num.num

    for c in parser.connections.values():
        link_occupied[frozenset({c.a, c.b})] = 0

    while any(drone.current_hub != end for drone in drones):
        for drone in drones:
            if drone.next_hub is not None:
                if drone.next_hub == end:
                    link_occupied[drone.current_hub] -= 1
                    drone.current_hub = end
                    continue
                current = drone.current_hub
                next = drone.next_hub
                edge = frozenset({current, next})
                if hub_occupied[next] < parser.hubs[next].max_drone_capacity:
                    if link_occupied[edge] < parser.connections[edge].max_link_capacity:
                        hub_occupied[drone.current_hub] -= 1
                        drone.current_hub = drone.next_hub
                        hub_occupied[drone.current_hub] += 1
                        link_occupied[edge] += 1

                        print(link_occupied, hub_occupied, drone.current_hub, drone.next_hub)


drone_trafficing("/home/pidi/Documents/My github repos/Python-42-school/Fly-in/maps/medium/03_priority_puzzle.txt")