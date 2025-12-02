n, m = map(int, input().split())
boss = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for index, item in enumerate(boss):
    if index == 0:
        continue
    graph[item].append(index+1)

dp = [0 for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    dp[a] += b

for i in range(1, n + 1):
    while graph[i]:
        num = graph[i].pop()
        dp[num] += dp[i]

for i in range(1, len(dp)):
    print(dp[i], end=" ")