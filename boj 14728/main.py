n, t = map(int, input().split())
time = list()
score = list()
for _ in range(n):
    a, b = map(int, input().split())
    time.append(a)
    score.append(b)

dp = [[0 for _ in range(t + 1)] for _ in range(n + 1)]

for i in range(1, n+1):
    for j in range(1, t+1):
        if j >= time[i-1]:
            dp[i][j] = max(dp[i - 1][j - time[i-1]] + score[i-1], dp[i - 1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])