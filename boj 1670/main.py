n = int(input())
dp = [0 for _ in range(n + 1)]
dp[0] = 1
dp[2] = 1
for i in range(4, n + 1, 2):
    for j in range(i // 2):
        dp[i] += (dp[j * 2] * dp[i - j * 2 - 2]) % 987654321
        dp[i] = dp[i] % 987654321
print(dp[n])