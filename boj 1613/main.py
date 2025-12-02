import sys

n, k = map(int, input().split())
dp = [[sys.maxsize for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    dp[i][i] = 0

for _ in range(k):
    a, b = map(int, input().split())
    dp[a][b] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

s = int(input())
for _ in range(s):
    a, b = map(int, input().split())
    if dp[a][b] == sys.maxsize and dp[b][a] == sys.maxsize:
        print(0)
    elif dp[a][b] < dp[b][a]:
        print(-1)
    else:
        print(1)
