from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
indegree = [0 for _ in range(n + 1)]
dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    indegree[a] += c
    graph[b].append([a, c])

queue = deque()
for index, item in enumerate(indegree):
    if index == 0:
        continue
    if item == 0:
        queue.append(index)

while queue:
    node = queue.popleft()
    for nxt, cost in graph[node]:
        indegree[nxt] -= cost
        if dp[node].count(0) == n + 1:
            dp[nxt][node] += cost
        else:
            for i in range(1, n + 1):
                dp[nxt][i] += dp[node][i] * cost
        if indegree[nxt] == 0:
            queue.append(nxt)

for i in range(len(dp[n])):
    if dp[n][i] != 0:
        print(i, dp[n][i])