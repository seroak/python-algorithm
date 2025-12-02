import sys
n, k = map(int, input().split())
coins = list()
for _ in range(n):
    coin = int(input())
    coins.append(coin)
dp = [sys.maxsize for _ in range(k + 1)]
dp[0] = 0
for i in range(1, k + 1):
    for c in coins:
        if i >= c:
            dp[i] = min(dp[i], dp[i - c] + 1)

if dp[k] == sys.maxsize:
    print(-1)
else:
    print(dp[k])