from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

for _ in range(m):
    a, b = map(int, input().split())
    queue = deque()
    visited = [-1] * (n + 1)
    queue.append(a)
    visited[a] = 0
    while queue:
        node = queue.popleft()
        for nxt, cost in graph[node]:
            if visited[nxt] == -1:
                visited[nxt] = visited[node] + cost
                queue.append(nxt)
    print(visited[b])
