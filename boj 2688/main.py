t = int(input())
dp = [[0 for _ in range(10)]for _ in range(66)]
for i in range(10):
    dp[0][i] = 1
for i in range(65):
    tmp = 0
    for j in range(10):
        tmp += dp[i][j]
        dp[i+1][j] = tmp

for _ in range(t):
    n = int(input())
    print(dp[n][-1])