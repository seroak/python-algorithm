from collections import deque

n, m, k = map(int, input().split())
board = [[0] * n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            board[i][j] = 1
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def bfs(x, y):
    count = 0
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True
    while queue:
        cx, cy = queue.popleft()
        count += 1
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if visited[nx][ny] is False and board[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append([nx, ny])

    return count


visited = [[False] * n for _ in range(m)]
count = 0

count_list = list()
for i in range(m):
    for j in range(n):
        if visited[i][j] is False and board[i][j] == 0:
            num = bfs(i, j)
            count += 1
            count_list.append(num)


print(count)
print(*sorted(count_list))