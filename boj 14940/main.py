from collections import deque

n, m = map(int, input().split())
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
board = list()
queue = deque()
visited = [[False] * m for _ in range(n)]
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(len(tmp)):
        if tmp[j] == 2:
            queue.append([i, j])
            visited[i][j] = False
    board.append(tmp)

ans = [[0] * m for _ in range(n)]
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] == 1 and visited[nx][ny] is False:
                ans[nx][ny] = ans[x][y] + 1
                visited[nx][ny] = True
                queue.append([nx, ny])
for i in range(n):
    for j in range(m):
        if visited[i][j] is False and board[i][j] == 1:
            ans[i][j] = -1
for i in ans:
    print(*i)
