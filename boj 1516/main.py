import sys
from collections import deque
input = sys.stdin.readline
n = int(input())

degree = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
back_graph = [[] for _ in range(n+1)]
cost = [0 for _ in range(n+1)]
for i in range(1, n+1):
    tmp = list(map(int, input().split()))
    cost[i] = tmp[0]
    for j in tmp[1:]:
        if j == -1:
            break
        graph[j].append(i)
        back_graph[i].append(j)
        degree[i] += 1
value = [0 for _ in range(n+1)]
queue = deque()
for i in range(1, len(degree)):
    if degree[i] == 0:
        queue.append(i)
while queue:
    cur = queue.popleft()
    value[cur] += cost[cur]
    for i in graph[cur]:
        degree[i] -= 1
        value[i] = max(value[cur], value[i])
        if degree[i] == 0:
            queue.append(i)

for i in value[1:]:
    print(i)
