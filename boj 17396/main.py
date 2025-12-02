import heapq
from collections import defaultdict

n, m = map(int, input().split())
sights = list(map(int, input().split()))
routes = defaultdict(list)
for _ in range(m):
    a, b, t = map(int, input().split())
    if ((sights[a] == 1) and (a != n - 1)) or ((sights[b] == 1) and (b != n - 1)):
        continue
    routes[a].append([t, b])
    routes[b].append([t, a])

inf = float("inf")
visited = [inf for _ in range(n)]
heap = []
for [dist, node] in routes[0]:
    heapq.heappush(heap, [dist, node])
visited[0] = 0
while heap:
    dist, cur = heapq.heappop(heap)

    if visited[cur] != inf:
        continue
    visited[cur] = dist
    for d, nxt in routes[cur]:
        if dist + d < visited[nxt]:
            heapq.heappush(heap, [dist + d, nxt])
if visited[n-1] == inf:
    print(-1)
else:
    print(visited[n-1])