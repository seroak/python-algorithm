from collections import deque

n, m = map(int, input().split())
board = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    board.append(tmp)
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
visited = [[0 for _ in range(m)] for _ in range(n)]
width_dict = dict()

def bfs(r, c, mark):
    queue = deque()
    queue.append([r, c])
    visited[r][c] = mark
    width = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = mark
                    width += 1
                    queue.append([nx, ny])
    return width

flag = 1
for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and visited[i][j] == 0:
            width = bfs(i, j, flag)
            width_dict[flag] = width
            flag += 1


answer = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            c = 0
            s = set()
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < n and 0 <= ny < m:
                    if visited[nx][ny] != 0:
                        s.add(visited[nx][ny])
            for q in s:
                c += width_dict[q]
            answer = max(answer, c+1)
print(answer)