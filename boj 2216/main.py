A, B, C = map(int, input().split())
X = input().strip()
Y = input().strip()
dp = [[-float('inf')] * (len(Y) + 1) for _ in range(len(X) + 1)]
dp[0][0] = 0

for i in range(len(X) + 1):
    for j in range(len(Y) + 1):
        if i < len(X) and j < len(Y):
            if X[i] == Y[j]:
                num = A
            else:
                num = C
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + num)
        if i < len(X):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + B)
        if j < len(Y):
            dp[i][j + 1] = max(dp[i][j + 1], dp[i][j] + B)

print(dp[-1][-1])