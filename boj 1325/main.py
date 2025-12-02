from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

ans = 0


def bfs(queue):
    global ans
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if visited[i] is False:
                visited[i] = True
                ans += 1
                queue.append(i)


t = list()
for i in range(1, n + 1):
    visited = [False] * (n + 1)
    visited[i] = True
    ans = 1
    queue = deque()
    queue.append(i)
    bfs(queue)
    t.append([ans, i])
t.sort(key=lambda x: (-x[0], x[1]))

for i in t:
    if t[0][0] == i[0]:
        print(i[1], end=" ")
    else:
        break
