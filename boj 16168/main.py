import sys
sys.setrecursionlimit(10**9)
v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (v+1)

def dfs(node):
    visited[node] = True
    for nxt in graph[node]:
        if visited[nxt] is False:
            dfs(nxt)
dfs(1)
for i in visited[1:]:
    if i is False:
        print("NO")
        exit(0)
odd_count = 0
for i in graph:
    if len(i) % 2 == 1:
        odd_count += 1
if odd_count == 0 or odd_count == 2:
    print("YES")
else:
    print("NO")