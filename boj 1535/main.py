n = int(input())
hp = list(map(int, input().split()))
happy = list(map(int, input().split()))

dp = [[0 for _ in range(100)] for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1, 100):
        # 체력을 담을 수 있을 때
        if j >= hp[i-1]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-hp[i-1]] + happy[i-1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])
