def dijkstra(graph, source, target):
    universal_nodes: set = set(graph.keys())
    node_distance: dict[str, int | float] = {}

    for s in universal_nodes:
        node_distance[s] = float("inf")

    node_distance[source] = 0


    
