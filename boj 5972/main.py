import sys
import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
dist = [sys.maxsize] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])
    graph[b].append([c, a])
heap = list()
heap.append([0, 1])
while heap:
    cost, node = heapq.heappop(heap)
    if dist[node] < cost:
        continue
    dist[node] = cost
    for c, nxt in graph[node]:
        if dist[node] + c < dist[nxt]:
            heapq.heappush(heap, ([dist[node] + c, nxt]))

print(dist[-1])
