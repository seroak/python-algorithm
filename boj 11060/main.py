import sys

n = int(input())
arr = list(map(int, input().split()))
dp = [sys.maxsize for _ in range(n)]
dp[0] = 0
for index, item in enumerate(arr):
    for i in range(1, item + 1):
        if index + i > n-1:
            continue
        dp[index + i] = min(dp[index] + 1, dp[index + i])
if dp[-1] == sys.maxsize:
    print(-1)
else:
    print(dp[-1])
