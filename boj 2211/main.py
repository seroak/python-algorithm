import sys
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append([cost, b])
    graph[b].append([cost, a])
heap = list()
heapq.heappush(heap, [0, 1])
dist = [sys.maxsize for _ in range(n + 1)]
dist[1] = 0
parent = [0 for _ in range(n + 1)]

while heap:
    c, node = heapq.heappop(heap)
    if dist[node] < c:
        continue

    for cost, nxt in graph[node]:
        if c + cost < dist[nxt]:  # 최단 거리 갱신될 때만 부모 정보 업데이트
            dist[nxt] = c + cost
            parent[nxt] = node  # 최단 거리 갱신 시 부모 노드 설정
            heapq.heappush(heap, [dist[nxt], nxt])

print(n - 1)
for i in range(2, n + 1):
    print(i, parent[i])
