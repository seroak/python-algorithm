n, m = map(int, input().split())
# 왼쪽 오른쪽으로는 누적합 시키면서 누적 시키고
# 위에서 오는건 최댓값을 택한다
table = [list(map(int, input().split())) for _ in range(n)]

dp = [0 for _ in range(m)]
dp[0] = table[0][0]
for i in range(1, m):
    dp[i] = dp[i-1] + table[0][i]

for i in range(1, n):
    right = [0 for _ in range(m)]
    right[0] = table[i][0] + dp[0]
    for j in range(1, m):
        right[j] = max(right[j-1], dp[j]) + table[i][j]
    left = [0 for _ in range(m)]
    left[-1] = table[i][-1] + dp[-1]
    for j in range(m-2, -1, -1):
        left[j] = max(left[j+1], dp[j]) + table[i][j]
    for j in range(m):
        dp[j] = max(right[j], left[j])

print(dp[-1])
