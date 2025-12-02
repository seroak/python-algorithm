from collections import deque

w, h = map(int, input().split())
# h * w
board = [list(map(str, input().rstrip())) for _ in range(h)]
c = list()
for i in range(h):
    for j in range(w):
        if board[i][j] == "C":
            c.append((i, j))
st = c[0]
en = c[1]
inf = float('inf')

route = [[[inf for _ in range(w)] for _ in range(h)] for _ in range(4)]
dx_dy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
queue = deque()
for i in range(4):
    queue.append((i, st[0], st[1]))
    route[i][st[0]][st[1]] = 0
while queue:
    d, x, y = queue.popleft()
    for i in range(4):
        nx = x + dx_dy[i][0]
        ny = y + dx_dy[i][1]
        if 0 <= nx < h and 0 <= ny < w:
            if board[nx][ny] != "*":
                if d == i:
                    cost = route[d][x][y]
                else:
                    cost = route[d][x][y] + 1
                if cost < route[i][nx][ny]:
                    route[i][nx][ny] = cost
                    queue.append((i, nx,ny))
mn = float("inf")
for i in range(4):
    mn = min(mn, route[i][en[0]][en[1]])
print(mn)
