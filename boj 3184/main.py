from collections import deque

r, c = map(int, input().split())
board = [list(map(str, input().rstrip())) for _ in range(r)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
visited = [[False] * c for _ in range(r)]


def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True
    escape = False
    wolf = 0
    sheep = 0
    if board[x][y] == "v":
        wolf += 1
    if board[x][y] == "o":
        sheep += 1
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                escape = True
                continue
            if visited[nx][ny] is True:
                continue
            if board[nx][ny] == "#":
                continue
            if board[nx][ny] == "v":
                wolf += 1
            if board[nx][ny] == "o":
                sheep += 1
            queue.append([nx, ny])
            visited[nx][ny] = True

    return wolf, sheep, escape


total_wolf = 0
total_sheep = 0
for i in range(r):
    for j in range(c):
        if visited[i][j] is False and board[i][j] != '#':
            wolf, sheep, escape = bfs(i, j)
            if escape is True:
                continue
            if sheep > wolf:
                total_sheep += sheep
            else:
                total_wolf += wolf
print(total_sheep, total_wolf)
