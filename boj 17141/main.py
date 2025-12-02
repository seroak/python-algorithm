from itertools import combinations
from collections import deque
import sys

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
virus = list()
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            virus.append([i, j])
answer = sys.maxsize
for comb in combinations(virus, m):
    queue = deque()
    time_board = [[-1 for _ in range(n)] for _ in range(n)]
    mx = 0
    for c in comb:
        queue.append(c)
        time_board[c[0]][c[1]] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if time_board[nx][ny] == -1 and (board[nx][ny] == 0 or board[nx][ny] == 2):
                    time_board[nx][ny] = time_board[x][y] + 1
                    queue.append([nx, ny])
    flag = False
    for i in range(n):
        for j in range(n):
            if (board[i][j] == 0 or board[i][j] == 2) and time_board[i][j] == -1:
                flag = True
            if time_board[i][j] != -1:
                mx = max(time_board[i][j], mx)

    if flag is False:
        answer = min(answer, mx)
if answer == sys.maxsize:
    print(-1)
else:
    print(answer)
