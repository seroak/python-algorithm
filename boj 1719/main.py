import sys
import heapq

n, m = map(int, input().split())
dp = [[sys.maxsize] * n for _ in range(n)]
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])
    graph[b].append([c, a])
for i in range(1, n + 1):
    heap = list()
    dist = [sys.maxsize] * (n + 1)
    dist[i] = 0
    route = [0] * (n + 1)
    for cost, nxt in graph[i]:
        # heap = [비용, 노드, 처음 집하장]
        heapq.heappush(heap, [cost, nxt, nxt])
    while heap:
        cost, node, first = heapq.heappop(heap)
        if dist[node] <= cost:
            continue
        dist[node] = cost
        route[node] = first
        for c, nxt in graph[node]:
            if dist[node] + c < dist[nxt]:
                heapq.heappush(heap, [dist[node] + c, nxt, first])
    for i in route[1:]:
        if i == 0:
            print("-", end=" ")
        else:
            print(i, end=" ")
    print()