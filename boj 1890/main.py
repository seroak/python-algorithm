import sys

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if i == n - 1 and j == n - 1:
            continue
        if dp[i][j] == 0:
            continue
        if i + board[i][j] < n:
            dp[i + board[i][j]][j] += dp[i][j]
        if j + board[i][j] < n:
            dp[i][j + board[i][j]] += dp[i][j]

print(dp[-1][-1])
