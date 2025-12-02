n = 5
m = 5
def colorTheGrid(m, n):
    dp = [[0 for _ in range(n)] for _ in range(m)]
    dp[0][0] = 3
    for i in range(1, n):
        dp[0][i] = 6
    for j in range(1, m):
        dp[j][0] = 6
    print(dp)
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1] + dp[i-1][j-1] + dp[i-1][j-1]
    print(dp[m-1][n-1])
    print(dp)
colorTheGrid(m, n)