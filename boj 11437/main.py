from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 부모 정보를 정수로 저장 (부모[node] = 부모 노드)
parent = [0] * (n + 1)
depths = [0] * (n + 1)
visited = [False] * (n + 1)

queue = deque([1])
visited[1] = True

while queue:
    node = queue.popleft()
    for neighbor in graph[node]:
        if not visited[neighbor]:
            visited[neighbor] = True
            depths[neighbor] = depths[node] + 1
            parent[neighbor] = node  # 리스트 대신 바로 정수로 저장
            queue.append(neighbor)

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    # 두 노드의 깊이를 맞추기
    while depths[a] > depths[b]:
        a = parent[a]
    while depths[b] > depths[a]:
        b = parent[b]
    # 공통 조상이 나올 때까지 부모 방향으로 올라가기
    while a != b:
        a = parent[a]
        b = parent[b]
    print(a)