from src.drone_brain.dijkstra import dijkstra, path_maker
from src.Parsers.map_parser import MapParser
from src.drone_brain.graph import Graph


def main() -> None:

    x = MapParser("/home/pidi/Documents/My github repos/Python-42-school/Fly-in/maps/hard/02_capacity_hell.txt")
    x.parse()
    graph = Graph(x)

    total, next = dijkstra(graph, x.end_hub.name)
    p = path_maker(x.start_hub.name, x.end_hub.name, next)

    print(p)
    print("Total cost:", total[x.start_hub.name])

main()
