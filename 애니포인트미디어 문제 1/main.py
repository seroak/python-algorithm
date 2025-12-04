from collections import deque


def solution(hax_grid, points):
    rows = len(hax_grid)
    cols = len(hax_grid[0])
    # --- 1. 이웃 찾기 ---
    def get_neighbors(r, c):
        if c % 2 == 0:  # 짝수 열 규칙
            dr_dc = [(-1, 0), (1, 0), (-1, -1), (0, -1), (-1, 1), (0, 1)]
        else:  # 홀수 열 규칙
            dr_dc = [(-1, 0), (1, 0), (0, -1), (1, -1), (0, 1), (1, 1)]

        neighbors = []
        for dr, dc in dr_dc:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                neighbors.append((nr, nc))
        return neighbors

    # --- 2. 선 긋기 (BFS) ---
    def get_line_bfs(start, end):
        if start == end:
            return [start]

        queue = deque([start])
        visited = {start: None}

        while queue:
            curr = queue.popleft()
            if curr == end:
                break

            for neighbor in get_neighbors(*curr):
                if neighbor not in visited:
                    visited[neighbor] = curr
                    queue.append(neighbor)
        print(visited)
        path = []
        curr = end
        while curr is not None:
            path.append(curr)
            curr = visited.get(curr)
        return path

    shape_cells = set()

    if len(points) == 1:
        shape_cells.add(tuple(points[0]))
    else:
        for i in range(len(points)):
            p1 = tuple(points[i])
            p2 = tuple(points[(i + 1) % len(points)])

            line_path = get_line_bfs(p1, p2)
            for cell in line_path:
                shape_cells.add(cell)

    total_sum = 0
    calculated_neighbors = set()

    # shape_cells는 이제 '테두리 선'만 들어있습니다.
    for r, c in shape_cells:
        for nr, nc in get_neighbors(r, c):
            if (nr, nc) not in shape_cells and (nr, nc) not in calculated_neighbors:
                total_sum += hax_grid[nr][nc]
                calculated_neighbors.add((nr, nc))

    return total_sum


hax_grid = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [4, 4, 4, 4, 4], [8, 8, 8, 8, 8], [16, 16, 16, 16, 16],
            [32, 32, 32, 32, 32]]
points = [[2, 1], [4, 1]]

print(solution(hax_grid, points))
