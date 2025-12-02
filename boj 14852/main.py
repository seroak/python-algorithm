n = int(input())
dp = [0 for _ in range(1000001)]
dp[0] = 1
dp[1] = 2
dp[2] = 7
acc_sum = 0
if n < 3:
    print(dp[n])
else:
    for i in range(3, n+1):
        dp[i] = (dp[i-1] * 2 + dp[i-2] * 3 + dp[i-3] * 2 + acc_sum) % 1000000007
        acc_sum += dp[i-3] * 2
    print(dp[n])