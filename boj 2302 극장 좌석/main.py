n = int(input())
m = int(input())
dp = [[0, 0] for _ in range(n + 2)]  # 0은 자리 지킴 1은 움직임


for i in range(m):
    fixed_seat = int(input())
    dp[fixed_seat][1] = -1
    dp[fixed_seat + 1][1] = -1
dp[1][0] = 1
dp[1][1] = 0
for i in range(2, n + 1):
    if dp[i][1] == -1:
        dp[i][0] = dp[i - 1][0] + dp[i - 1][1]
        dp[i][1] = 0
    else:
        dp[i][0] = dp[i - 1][0] + dp[i - 1][1]
        dp[i][1] = dp[i - 1][0]
print(dp[n][0] + dp[n][1])
