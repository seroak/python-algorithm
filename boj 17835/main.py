import sys
import heapq
input = sys.stdin.readline
n, m, k = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    u, v, c = map(int, input().split())
    graph[v].append([u, c])
k = list(map(int, input().split()))

dist = [sys.maxsize for _ in range(n+1)]
for i in k:
    graph[0].append([i,0])
    dist[i] = 0

def dijkstra(node):
    queue = []
    for edge in graph[node]:
        nxt, cost = edge
        heapq.heappush(queue, (cost, nxt))

    while queue:
        cost, cur = heapq.heappop(queue)
        if dist[cur] < cost:
            continue
        for nxt, c in graph[cur]:
            if dist[nxt] > cost + c:
                dist[nxt] = cost + c
                heapq.heappush(queue, (dist[nxt], nxt))
dijkstra(0)
mx = max(dist[1:])
for i in range(len(dist[1:])):
    if mx == dist[i+1]:
        print(i+1)
        print(mx)
        break