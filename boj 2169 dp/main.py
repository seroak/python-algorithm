n, m = map(int, input().split())
graph = list()
for _ in range(n):
    graph.append(list(map(int, input().split())))
dp = [[0 for _ in range(m)] for _ in range(n)]
dp[0][0] = graph[0][0]
# 첫줄 전부 더하기
for i in range(1, m):
    dp[0][i] = graph[0][i]+dp[0][i-1]

# 첫줄 마지막 줄 빼고 양쪽으로 더하기
for i in range(1, n):
    # 오른쪽으로 더하기
    right = [0 for _ in range(m)]
    right[0] = dp[i-1][0] + graph[i][0]
    for j in range(1, m):
        right[j] = max(right[j-1] + graph[i][j], dp[i-1][j] + graph[i][j])

    # 왼쪽으로 더하기
    left = [0 for _ in range(m)]
    left[m-1] = dp[i-1][-1] + graph[i][-1]
    for j in range(m-1, 0, -1):
        left[j-1] = max(left[j] + graph[i][j-1], dp[i-1][j-1] + graph[i][j-1])

    for j in range(m):
        dp[i][j] = max(right[j], left[j])

print(dp[n-1][m-1])