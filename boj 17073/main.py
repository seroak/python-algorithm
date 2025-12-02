from collections import deque

n, w = map(int, input().split())
graph = [[] for _ in range(n + 1)]

divide_list = []
total_leaf = 0


def bfs(node, visited):
    global total_leaf
    queue = deque()
    queue.append((node, 0, 1))
    while queue:
        cur, cur_depth, divide_num = queue.popleft()
        is_leaf = True
        for nxt in graph[cur]:
            if visited[nxt] is False:
                is_leaf = False
                visited[nxt] = True
                if cur_depth == 0:
                    queue.append((nxt, cur_depth + 1, divide_num * len(graph[cur])))
                else:
                    queue.append((nxt, cur_depth + 1, divide_num * (len(graph[cur])-1)))
        if is_leaf:

            total_leaf += 1
            divide_list.append(divide_num)


for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
visited[1] = True
bfs(1, visited)

a = 0
for i in divide_list:
    a += w / (i * len(divide_list))
print(a)
