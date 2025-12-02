import heapq

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
heap = list()
connected = [False for _ in range(n)]
ans = 0
for i in range(n):
    if graph[0][i] != 0:
        heapq.heappush(heap, [graph[0][i], i])
connected[0] = True
while heap:
    cost, node = heapq.heappop(heap)
    if not connected[node]:
        ans += cost
        connected[node] = True
        for i in range(n):
            if graph[node][i] != 0 and not connected[i]:
                heapq.heappush(heap, [graph[node][i], i])
print(ans)