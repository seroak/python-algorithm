from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
island = [[0] * m for _ in range(n)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def bfs(x, y, count):
    queue = deque()
    queue.append([x, y])
    island[x][y] = count
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = dx[i] + cx
            ny = dy[i] + cy
            if 0 <= nx < n and 0 <= ny < m:
                if island[nx][ny] == 0 and board[nx][ny] == 1:
                    island[nx][ny] = count
                    queue.append([nx, ny])


island_count = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and island[i][j] == 0:
            island_count += 1
            bfs(i, j, island_count)
parent = [i for i in range(island_count + 1)]

graph = list()
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            for k in range(4):
                nx = i
                ny = j
                count = 0
                find_island = False
                while True:
                    nx = dx[k] + nx
                    ny = dy[k] + ny
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        find_island = False
                        break
                    if board[nx][ny] != 0:
                        find_island = True
                        break
                    count += 1
                if find_island is True:
                    if count > 1:
                        graph.append([count, island[i][j], island[nx][ny]])




def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


graph.sort()

ans = 0
for count, a, b in graph:
    a = find_parent(a)
    b = find_parent(b)
    if a == b:
        continue
    union_parent(a, b)
    ans += count

tmp = find_parent(1)
for i in range(2, len(parent)):
    if tmp != find_parent(i):
        print(-1)
        break
else:
    print(ans)
