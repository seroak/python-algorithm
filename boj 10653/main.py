n, k = map(int, input().split())
check_point = []
for i in range(n):
    a, b = map(int, input().split())
    check_point.append([a, b])
INF = float("inf")
dp = [[INF] * n for _ in range(k+1)]
dp[0][0] = 0

for i in range(k+1):
    for j in range(n):
        for q in range(j):
            if q > k:
                break
            if j - q - 1 < 0:
                break

            dp[i][j] = min(dp[i - q][j - q - 1] + abs(check_point[j - q - 1][0] - check_point[j][0]) + abs(
                check_point[j - q - 1][1] - check_point[j][1]), dp[i][j])

print(dp[-1][-1])
