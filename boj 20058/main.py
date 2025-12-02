from collections import deque

n, q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(2 ** n)]
L = list(map(int, input().split()))


def rotate_90(x, y, length):
    col = (length - 1) - x
    return y, col


dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for l in L:
    square = 2 ** l
    new_board = [[0 for _ in range(2 ** n)] for _ in range(2 ** n)]
    if square > 1:
        for i in range(2 ** n):
            for j in range(2 ** n):
                row_level = i // square
                col_level = j // square
                x, y = rotate_90(i % square, j % square, square)
                rotate_x = x + row_level * square
                rotate_y = y + col_level * square

                new_board[rotate_x][rotate_y] = board[i][j]
    else:
        for i in range(2 ** n):
            for j in range(2 ** n):
                new_board[i][j] = board[i][j]
    temp_board = [row[:] for row in new_board]  # deepcopy 효과

    for i in range(2 ** n):
        for j in range(2 ** n):
            if new_board[i][j] > 0:
                count = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < 2 ** n and 0 <= ny < 2 ** n:
                        if new_board[nx][ny] > 0:
                            count += 1
                if count < 3:
                    temp_board[i][j] -= 1  # 새로운 배열에 저장

    new_board = temp_board  # 업데이트 완료

    board = new_board
total = 0
for i in board:
    for j in i:
        total += j
print(total)
visited = [[False for _ in range(2 ** n)] for _ in range(2 ** n)]


def bfs(r, c):
    queue = deque()
    queue.append((r, c))
    visited[r][c] = True
    count = 0
    while queue:
        x, y = queue.popleft()
        count += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 2 ** n and 0 <= ny < 2 ** n:
                if board[nx][ny] > 0 and visited[nx][ny] is False:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
    return count


mx = 0
for i in range(2 ** n):
    for j in range(2 ** n):
        if board[i][j] > 0:
            ans = bfs(i, j)
            mx = max(mx, ans)
print(mx)
