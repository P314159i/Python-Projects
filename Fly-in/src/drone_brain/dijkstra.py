from .graph import Graph
from src.Parsers.parse_rules import Zones


def dijkstra(
        graph: Graph,
        target: str) -> tuple[
            dict[str, int | float],
            dict[str, str]
            ]:
    ''' smarter ones go backwards '''

    totalCost_sofar: dict[str, int | float] = {}
    unvisited: set[str] = set(graph.neighbours.keys())
    next_hop: dict[str, str] = {}

    if target not in graph.neighbours:
        raise ValueError(f"Wait... there is no '{target}' target hub to go to!")
    for node in graph.neighbours:
        totalCost_sofar[node] = float("inf")

    totalCost_sofar[target] = 0

    while unvisited:
        current = min(unvisited, key=lambda unvis: totalCost_sofar[unvis])
        unvisited.remove(current)

        if totalCost_sofar[current] == float("inf"):
            break

        for neighbour in graph.neighbours[current]:
            if neighbour not in unvisited:
                continue

            new_totalCost_sofar = (
                totalCost_sofar[current] # acuumulted until where we're at
                + graph.neighbours[neighbour][current] # moving cost of wehre we're at -> neighbour
            )

            if new_totalCost_sofar == totalCost_sofar[neighbour]:
                if graph.hubs[current].zone == Zones.PRIORITY:
                    next_hop[neighbour] = current
            if new_totalCost_sofar < totalCost_sofar[neighbour]:
                totalCost_sofar[neighbour] = new_totalCost_sofar
                next_hop[neighbour] = current # stores next best step for EVERY hub

    return totalCost_sofar, next_hop


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
