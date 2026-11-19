from src.Parsers.map_parser import MapParser
from .simul_rules import Drone
from pathlib import Path
from src.drone_brain.graph import Graph
from src.drone_brain.dijkstra import dijkstra, path_maker


def _drone_constructor(
        num_drones: int, start: str, path: list[str]
        ) -> list[Drone]:

    if not path:
        return ValueError("No path from start to end found by the algorithm")

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
    num_drones: int = parser.num.num # first num is pydantic Num model
    start: str = parser.start_hub.name
    end: str = parser.end_hub.name
    hub_drones: list[Drone] = []

    _, next_hop = dijkstra(graph, end)
    path = path_maker(start, end, next_hop)

    drones = _drone_constructor(num_drones, start, end, path)

    while any(drone.current_hub != end for drone in drones):
        for drone in drones:
            if len(hub_drones) < drone.next_hub:
                if drone.next_hub != None:
                    drone.current_hub = drone.next_hub
                    hub_drones.append(drone)

