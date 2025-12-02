import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]   # BFS용: graph[u]에 v들만 저장
edges = []                           # (u, v, w) 목록
INF = float('-inf')
dist = [INF] * (n + 1)
prev = [-1] * (n + 1)

for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))
    graph[u].append(v)

# Bellman-Ford (최대 경로 버전)
dist[1] = 0
for _ in range(n - 1):
    updated = False
    for u, v, w in edges:
        if dist[u] != INF and dist[v] < dist[u] + w:
            dist[v] = dist[u] + w
            prev[v] = u
            updated = True
    if not updated:
        break

# n번째 반복에서 완화 가능한 정점들 수집 -> 양의 사이클의 영향권
affected = [False] * (n + 1)
for u, v, w in edges:
    if dist[u] != INF and dist[v] < dist[u] + w:
        affected[v] = True

# affected 정점들에서 출발해 도착점(n)으로 갈 수 있는지 검사
q = deque([i for i in range(1, n + 1) if affected[i]])
visited = [False] * (n + 1)
for x in q:
    visited[x] = True

while q:
    x = q.popleft()
    if x == n:
        print(-1)
        sys.exit(0)
    for nx in graph[x]:
        if not visited[nx]:
            visited[nx] = True
            q.append(nx)

# 도달 불가(경로 자체가 없음)
if dist[n] == INF:
    print(-1)
    sys.exit(0)

# 경로 복원 (안전 장치: 길이가 n을 넘지 않도록)
path = []
cur = n
for _ in range(n):   # 최대 n번만 시도
    path.append(cur)
    if cur == 1:
        break
    cur = prev[cur]
else:
    # prev를 타고 올라갔는데 1에 도달 못하면 문제 (안전하게 -1)
    print(-1)
    sys.exit(0)

path.reverse()
print(*path)