import sys
input = sys.stdin.readline
n = int(input())
arr = list()
for i in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])

dp = [0 for _ in range(n+1)]
for i in range(n - 1, -1, -1):
    # 상담이 가능 할때
    if i + arr[i][0] <= n:

        dp[i] = arr[i][1] + dp[i + arr[i][0]]
    dp[i] = max(dp[i+1], dp[i])
print(dp[0])
