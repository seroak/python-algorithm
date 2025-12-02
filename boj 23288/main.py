from collections import deque

n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
row_queue = deque([4, 6, 3, 1])
col_queue = deque([5, 6, 2, 1])

# 동 북 서 남
dx_dy = ((0, 1), (-1, 0), (0, -1), (1, 0))
dist = 0
# 주사위의 현재 위치
x, y = 0, 0


def bfs(r, c):
    queue = deque()
    queue.append((r, c))
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[r][c] = True
    result = 1
    number = board[r][c]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx_dy[i][0]
            ny = y + dx_dy[i][1]
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == number and visited[nx][ny] is False:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    result += 1

    return result * number


score = 0

for _ in range(k):
    nx = x + dx_dy[dist][0]
    ny = y + dx_dy[dist][1]
    if 0 <= nx < n and 0 <= ny < m:
        x = nx
        y = ny
    else:
        dist = (dist + 2) % 4
        x += dx_dy[dist][0]
        y += dx_dy[dist][1]

    # 동
    if dist == 0:
        row_queue.rotate(-1)
        col_queue[1] = row_queue[1]
        col_queue[3] = row_queue[3]
    # 북
    elif dist == 1:
        col_queue.rotate(-1)
        row_queue[1] = col_queue[1]
        row_queue[3] = col_queue[3]
    # 서
    elif dist == 2:
        row_queue.rotate(1)
        col_queue[1] = row_queue[1]
        col_queue[3] = row_queue[3]
    # 남
    elif dist == 3:
        col_queue.rotate(1)
        row_queue[1] = col_queue[1]
        row_queue[3] = col_queue[3]

    if row_queue[1] > board[x][y]:
        dist = (dist + 3) % 4  # 반시계 방향 (dist - 1과 동일)
    elif row_queue[1] < board[x][y]:
        dist = (dist + 1) % 4  # 시계 방향

    score += bfs(x, y)

print(score)
