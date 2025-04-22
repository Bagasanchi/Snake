from pygame.math import Vector2
from collections import deque

def bfs(start, goal, grid_size):
    directions = [Vector2(1,0), Vector2(-1,0), Vector2(0,1), Vector2(0,-1)]
    queue = deque()
    queue.append((start, []))
    visited = set()
    visited.add((start.x, start.y))  # Use tuple for hashable

    goal_tuple = (goal.x, goal.y)

    while queue:
        current, path = queue.popleft()
        current_tuple = (current.x, current.y)

        if current_tuple == goal_tuple:
            return path

        for d in directions:
            neighbor = current + d
            neighbor_tuple = (neighbor.x, neighbor.y)
            if (0 <= neighbor.x < grid_size and 0 <= neighbor.y < grid_size and
                neighbor_tuple not in visited):
                visited.add(neighbor_tuple)
                queue.append((neighbor, path + [d]))

    return []
