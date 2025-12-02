import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = map(int, input().split())
s, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]
routes = []
for _ in range(m):
    h1, h2, k = map(int, input().split())
    routes.append([k, h1, h2])
routes.sort(reverse=True)
parent = [i for i in range(n + 1)]


def find_parent(a):
    if a != parent[a]:
        parent[a] = find_parent(parent[a])
    return parent[a]


def union_parent(origin_a, origin_b, k):
    a = find_parent(origin_a)
    b = find_parent(origin_b)
    if a != b:
        graph[origin_a].append([origin_b, k])
        graph[origin_b].append([origin_a, k])
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for k, h1, h2 in routes:
    union_parent(h1, h2, k)

inf = float("inf")
queue = deque()
visited = [inf for _ in range(n+1)]
queue.append(s)
visited[s] = 1000001
while queue:
    cur = queue.popleft()
    for nxt, cost in graph[cur]:
        if visited[nxt] != inf:
            continue
        visited[nxt] = min(cost, visited[cur])
        queue.append(nxt)

print(0 if visited[e] == inf else visited[e])