from collections import deque

n, m = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
x1 = x1 - 1
y1 = y1 - 1
x2 = x2 - 1
y2 = y2 - 1

board = []
for i in range(n):
    tmp = list(map(str, input().rstrip()))
    board.append(tmp)

queue = deque()
queue.append([x1, y1])
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
visited = [[False] * m for _ in range(n)]
visited[x1][y1] = True
find_choco = False
answer = 0
while queue:
    wave_zero = []
    new_queue = deque()
    while queue:
        x, y = queue.popleft()
        if x == x2 and y == y2:
            find_choco = True
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] is False:
                    if board[nx][ny] == "0":
                        wave_zero.append([nx, ny])
                        queue.append([nx, ny])
                        visited[nx][ny] = True
                    if board[nx][ny] == "1" or board[nx][ny] == "#":
                        new_queue.append([nx, ny])
                        visited[nx][ny] = True
    if find_choco:
        break
    while wave_zero:
        x, y = wave_zero.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] is False:
                    if board[nx][ny] == "1" or board[nx][ny] == "#":
                        visited[nx][ny] = True
                        new_queue.append([nx, ny])
    queue = new_queue
    answer += 1

print(answer)
