n, m = map(int, input().split())
board = []
for i in range(n):
    tmp = list(map(str, input().rstrip()))
    board.append(tmp)
visited = [[0] * m for _ in range(n)]


def is_exit(x, y, tracking):

    while True:

        # 탈출 성공
        if x < 0 or x >= n or y < 0 or y >= m:
            return [True, tracking]
        # 계속 같은 곳을 돌고 있음
        if (x, y) in tracking:
            return [False, tracking]
        # 성공한 위치에 왔을 때
        if visited[x][y] == 1:
            return [True, tracking]
        # 실패한 위치에 있을 때
        if visited[x][y] == 2:
            return [False, tracking]
        tracking.add((x, y))
        if board[x][y] == "U":
            x -= 1
            continue
        if board[x][y] == "R":
            y += 1
            continue
        if board[x][y] == "D":
            x += 1
            continue
        if board[x][y] == "L":
            y -= 1
            continue


for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:

            is_success, tracking = is_exit(i, j, set())
            if is_success:
                for r, c in list(tracking):
                    visited[r][c] = 1
            else:
                for r, c in list(tracking):
                    visited[r][c] = 2
ans = 0
for i in visited:
    for j in i:
        if j == 1:
            ans += 1
print(ans)