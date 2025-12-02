import sys

input = sys.stdin.readline

t, w = map(int, input().split())
data = [0]
for _ in range(t):
    x = int(input())
    data.append(x)
dp = [[0] * (w + 1) for _ in range(t + 1)]

for i in range(1, t + 1):
    if data[i] == 1:
        dp[i][0] = dp[i-1][0] + 1
    else:
        dp[i][0] = dp[i-1][0]
    for j in range(1, w + 1):
        # 움직여서 먹을 수 있는 경우
        if (data[i] == 1 and j % 2 == 0) or (data[i] == 2 and j % 2 == 1):
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + 1
        else:
            dp[i][j] = dp[i-1][j]
print(max(dp[t]))