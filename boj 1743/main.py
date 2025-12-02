from collections import deque

n, m, k = map(int, input().split())
board = [[0] * (m + 1) for _ in range(n + 1)]
for _ in range(k):
    x, y = map(int, input().split())
    board[x][y] = 1
visited = [[False] * (m + 1) for _ in range(n + 1)]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True
    ans = 0
    while queue:
        cx, cy = queue.popleft()
        ans += 1
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 < nx <= n and 0 < ny <= m:
                if visited[nx][ny] is False and board[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append([nx, ny])
    return ans


mx = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if board[i][j] == 1 and visited[i][j] is False:
            tmp = bfs(i, j)
            mx = max(mx, tmp)

print(mx)