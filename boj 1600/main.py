import sys
input = sys.stdin.readline
from collections import deque
k = int(input())
w, h = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(h)]

dxdy = [[0, 1], [-1, 0], [0, -1], [1, 0]]
jump_dxdy =[[-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2]]
dp = [[[-1 for _ in range(w)] for _ in range(h)] for _ in range(k+1)]
print(dp)
que = deque()
# (x위치, y위치, 움직인 횟수, 점프를 한 횟수)
que.append((0, 0, 0, 0))
dp[0][0][0] = 0
while que:
    x, y, move, jump = que.popleft()

    for i in dxdy:
        dx, dy = i
        nx = x + dx
        ny = y + dy
        if 0 <= nx < h and 0 <= ny < w:
            if board[nx][ny] == 1:
                continue
            # 처음 방문한 위치일 때
            if dp[jump][nx][ny] == -1:
                dp[jump][nx][ny] = move + 1
                que.append((nx, ny, move + 1, jump))
            # 다시 한번 방문한 위치일 때
            else:
                # 다시 한번 방문을 했는데 더 최단거리로 업데이트가 가능하면 갱신
                if dp[jump][nx][ny] > move + 1:
                    dp[jump][nx][ny] = move + 1
                    que.append((nx, ny, move + 1, jump))
    if jump < k:
        for i in jump_dxdy:
            dx, dy = i
            nx = x + dx
            ny = y + dy
            if 0 <= nx < h and 0 <= ny < w:
                if board[nx][ny] == 1:
                    continue
                # 처음 방문한 위치일 때
                if dp[jump+1][nx][ny] == -1:
                    dp[jump+1][nx][ny] = move + 1
                    que.append((nx, ny, move + 1, jump+1))
                # 다시 한번 방문한 위치일 때
                else:
                    # 다시 한번 방문을 했는데 더 최단거리로 업데이트가 가능하면 갱신
                    if dp[jump+1][nx][ny] > move + 1:
                        dp[jump+1][nx][ny] = move + 1
                        que.append((nx, ny, move + 1, jump+1))

mn = sys.maxsize
for i in range(len(dp)):
    tmp_mn = dp[i][h-1][w-1]
    if dp[i][h-1][w-1] == -1:
        continue
    if tmp_mn < mn:
        mn = tmp_mn

if mn == sys.maxsize:
    print(-1)
else:
    print(mn)