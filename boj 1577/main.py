n, m = map(int, input().split())
k = int(input())
road = dict()
for i in range(k):
    a, b, c, d = map(int, input().split())
    road[(a, b, c, d)] = True
    road[(c, d, a, b)] = True

dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
dp[0][0] = 1
for i in range(n + 1):
    for j in range(m + 1):
        if i == 0 and j == 0:
            continue
        if i - 1 < 0:
            if road.get((i, j, i, j - 1)) is None:
                dp[i][j] += dp[i][j - 1]
        elif j - 1 < 0:
            if road.get((i, j, i - 1, j)) is None:
                dp[i][j] = dp[i - 1][j]
        else:
            if road.get((i, j, i - 1, j)) is None:
                dp[i][j] += dp[i - 1][j]
            if road.get((i, j, i, j - 1)) is None:
                dp[i][j] += dp[i][j - 1]

print(dp[-1][-1])
