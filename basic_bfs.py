from collections import deque

def bfs(start, goal):
    queue = deque()
    queue.append((start, [start]))  # (current_node, path_so_far)
    visited = set()
    visited.add(start)

    while queue:
        current, path = queue.popleft()

        if current == goal:
            print("Found goal:", goal)
            print("Path:", path)
            print("Steps:", len(path) - 1)
            return path

        neighbors = [current + 1, current * 2]
        for n in neighbors:
            if n <= 100 and n not in visited:  # limit to reasonable range
                visited.add(n)
                queue.append((n, path + [n]))

    print("Goal not reachable")
    return []

bfs(1, 100)