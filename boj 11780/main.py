import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
dp = [[sys.maxsize for _ in range(n + 1)] for _ in range(n + 1)]
route = [[[] for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    if c < dp[a][b]:
        dp[a][b] = c
        route[a][b] = [a, b]
for i in range(1, n + 1):
    dp[i][i] = 0
    route[i][i].append(i)
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dp[i][k] + dp[k][j] < dp[i][j]:
                dp[i][j] = dp[i][k] + dp[k][j]
                route[i][j] = route[i][k] + route[k][j][1:]


for i in range(1, n + 1):
    print(' '.join(str(dp[i][j]) if len(route[i][j]) != 0 else '0' for j in range(1, n + 1)))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j or len(route[i][j]) == 0:
            print(0)
        else:
            print(len(route[i][j]), *route[i][j])
