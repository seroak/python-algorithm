import sys
from collections import deque

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
num = 1
while True:
    n = int(input())
    if n == 0:
        break
    board = [list(map(int, input().split())) for _ in range(n)]
    vis = [[sys.maxsize for _ in range(n)] for _ in range(n)]
    vis[0][0] = board[0][0]
    queue = deque()
    queue.append([0, 0])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if vis[x][y] + board[nx][ny] < vis[nx][ny]:
                    vis[nx][ny] = vis[x][y] + board[nx][ny]
                    queue.append([nx, ny])

    print("Problem %d: %d" %(num, vis[n - 1][n - 1]))
    num += 1
