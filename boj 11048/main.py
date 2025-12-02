N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(M)] for _ in range(N)]
dp[0][0] = board[0][0]
for i in range(N):
    for j in range(M):
        if i + 1 < N and j + 1 < M:
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + board[i + 1][j + 1])
        if i + 1 < N:
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + board[i + 1][j])
        if j + 1 < M:
            dp[i][j + 1] = max(dp[i][j + 1], dp[i][j] + board[i][j + 1])

print(dp[-1][-1])
