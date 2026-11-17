from .graph import Graph


def dijkstra(
        graph: Graph,
        target: str) -> tuple[
            dict[str, int | float],
            dict[str, str]
            ]:
    ''' smarter ones go backwards '''

    costances: dict[str, int | float] = {}
    unvisited: set[str] = set(graph.neighbours.keys())
    next_hop: dict[str, str] = {}

    if target not in graph.neighbours:
        raise ValueError(f"Wait... there is no '{target}' target hub to go to!")
    for node in graph.neighbours:
        costances[node] = float("inf")

    costances[target] = 0

    while unvisited:
        current = min(unvisited, key=lambda node: costances[node])
        unvisited.remove(current)

        if costances[current] == float("inf"):
            break

        for neighbour in graph.neighbours[current]:
            if neighbour not in unvisited:
                continue

            new_costance = (
                costances[current]
                + graph.neighbours[neighbour][current]
            )

            if new_costance < costances[neighbour]:
                costances[neighbour] = new_costance
                next_hop[neighbour] = current

    return costances, next_hop


def path_maker(
        start: str,
        target: str,
        next_hop: dict[str, str]
    ) -> list[str]:
        ''' its my matrix's keymaker (no) '''

        path: list[str] = []
        current = start

        path.append(start)

        while current != target:
            if current not in next_hop:
                return []  # No path exists

            current = next_hop[current]
            path.append(current)

        return path
