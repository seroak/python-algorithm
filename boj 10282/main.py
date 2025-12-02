import sys
import heapq
t = int(input())
def dijkstra(node):
    heap = list()
    heapq.heappush(heap, [0, node])
    while heap:
        cost, edge = heapq.heappop(heap)
        if cost > dist[edge]:
            continue
        for c, n in graph[edge]:
            if c + cost < dist[n]:
                dist[n] = c + cost
                heapq.heappush(heap, [c+cost, n])
for i in range(t):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    dist = [sys.maxsize for _ in range(n+1)]
    for _ in range(d):
        a, b, cost = map(int, input().split())
        graph[b].append([cost, a])
    dist[c] = 0
    dijkstra(c)
    count = 0
    mx = 0
    for i in dist:
        if i != sys.maxsize:
            count += 1
            mx = max(i, mx)
    print(count, mx)