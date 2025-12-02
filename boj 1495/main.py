N, S, M = map(int, input().split())
volume = list(map(int, input().split()))
dp = [[False for _ in range(M + 1)] for _ in range(N + 1)]
dp[0][S] = True
for i in range(N):
    for j in range(M + 1):
        if dp[i][j] is True:
            if j - volume[i] >= 0:
                dp[i + 1][j - volume[i]] = True
            if j + volume[i] <= M:
                dp[i + 1][j + volume[i]] = True

answer = - 1
for i in range(M, -1, -1):
    if dp[N][i] is True:
        answer = i
        break
print(answer)