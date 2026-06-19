import heapq
import math
from data_structures.city_map import CityMap


def heuristic(
    pos1: tuple[float, float],
    pos2: tuple[float, float]
) -> float:
    """Calcula a Distância Euclidiana em linha reta."""
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)


def find_path(
    city_map: CityMap,
    start: int,
    goal: int,
) -> list[int]:

    if (start not in city_map.intersections or
            goal not in city_map.intersections):
        return []

    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from = {start: None}

    g_score = {start: 0}

    while frontier:
        _, current = heapq.heappop(frontier)

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        for neighbor in city_map.roads[current]:
            move_cost = 1
            tentative_g_score = g_score[current] + move_cost

            if (neighbor not in g_score or
                    tentative_g_score < g_score[neighbor]):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score

                pos_neighbor = city_map.intersections[neighbor]
                pos_goal = city_map.intersections[goal]

                h_cost = heuristic(pos_neighbor, pos_goal) * 0.0001

                f_score = tentative_g_score + h_cost
                heapq.heappush(frontier, (f_score, neighbor))

    return []
