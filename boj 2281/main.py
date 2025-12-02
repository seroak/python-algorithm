n, m = map(int, input().split())
names = list()
for _ in range(n):
    name = int(input())
    names.append(name)
dp = [[-1 for _ in range(m + 1)] for _ in range(n+1)]
dp[0][names[0]] = 0
for i in range(n-1):
    for j in range(1, m+1):
        if dp[i][j] != -1:
            if j + names[i+1] + 1 <= m:
                dp[i + 1][j + names[i+1] + 1] = dp[i][j]

            if dp[i + 1][names[i + 1]] != -1:
                dp[i + 1][names[i + 1]] = min(dp[i + 1][names[i + 1]], dp[i][j] + (m - j) ** 2)
            else:
                dp[i + 1][names[i + 1]] = dp[i][j] + (m - j) ** 2
answer = 1000000000
for i in range(1, m+1):
    if dp[n-1][i] != -1:
        answer = min(answer, dp[n-1][i])
print(answer)
