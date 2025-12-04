a, b, d, n = map(int, input().split())
dp = [0] * (n + 1)

dp[0] = 1
for i in range(a-1):
    dp[i+1] = dp[i]

for i in range(a, n+1):
    dp[i] = (dp[i-a] + dp[i-1]) % 1000
    if i >= b:
        dp[i] = dp[i] - dp[i-b]

if n >= d:
    print((dp[-1] - dp[n-d]) % 1000)
else:
    print(dp[-1])