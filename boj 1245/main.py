from collections import deque

n, m = map(int, input().split())
board = []
for _ in range(n):
    arr = list(map(int, input().split()))
    board.append(arr)
visited = [[False] * m for _ in range(n)]
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]
answer = 0


def bfs(r, c):
    global answer
    queue = deque()
    queue.append([r, c])
    top = board[r][c]
    is_top = True
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if top < board[nx][ny]:
                    is_top = False
                if top == board[nx][ny]:
                    if visited[nx][ny] is False:
                        visited[nx][ny] = True
                        queue.append([nx, ny])

    if is_top:
        answer += 1


for i in range(n):
    for j in range(m):
        if visited[i][j] is False:
            visited[i][j] = True
            bfs(i, j)

print(answer)
