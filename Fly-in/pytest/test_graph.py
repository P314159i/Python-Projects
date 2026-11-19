from src.Parsers.map_parser import MapParser
from src.drone_brain.graph import Graph
from src.drone_brain.dijkstra import dijkstra, path_maker


parser = MapParser("/home/pidi/Documents/My github repos/Python-42-school/Fly-in/maps/challenger/01_the_impossible_dream.txt")
parser.parse()

graph = Graph(parser)

costances, next_hop = dijkstra(graph, parser.end_hub.name)

path = path_maker(
    parser.start_hub.name,
    parser.end_hub.name,
    next_hop
)

print("DRONES:", parser.num)
print("START:", parser.start_hub.name)
print("END:", parser.end_hub.name)

print("\nHUBS:")
for name, hub in parser.hubs.items():
    print(name, hub.zone)

print("\nCONNECTIONS:")
for connection in parser.connections.values():
    print(connection)

print("\nGRAPH (neighbours and movement costs):")
for hub, neighbours in graph.neighbours.items():
    print(hub, "->", neighbours)

print("\nDIJKSTRA:")
print("Costs to goal:", costances)
print("Next hops:", next_hop)

print("\nFINAL PATH:", path)
print("PATH COST:", costances[parser.start_hub.name])