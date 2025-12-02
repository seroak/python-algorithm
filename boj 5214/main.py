from collections import deque

n, k, m = map(int, input().split())
graph = [[] for _ in range(n + m + 1)]
for q in range(m):
    route = list(map(int, input().split()))
    for i in range(len(route)):
        graph[route[i]].append(n + q + 1)
        graph[n + q + 1].append(route[i])

visited = [-1] * (n + m + 1)
queue = deque()
queue.append((1, 0))
visited[1] = 0
while queue:
    cur, cnt = queue.popleft()
    for i in graph[cur]:
        if visited[i] == -1:
            if cur <= n:
                visited[i] = cnt + 1
                queue.append((i, cnt + 1))
            else:
                visited[i] = cnt
                queue.append((i, cnt))
if visited[n] == -1:
    print(-1)
else:
    print(visited[n]+1)