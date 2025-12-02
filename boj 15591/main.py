n, q = map(int, input().split())
graph = [[] for _ in range(n + 1)]

def dfs(curr, stand):
    count = 0
    stack = [curr]
    visited[curr] = True

    while stack:
        node = stack.pop()
        for neighbor, cost in graph[node]:
            if not visited[neighbor] and cost >= stand:
                visited[neighbor] = True
                count += 1
                stack.append(neighbor)
    return count

# 그래프 입력
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

# 쿼리 처리
for _ in range(q):
    stand, start = map(int, input().split())
    visited = [False for _ in range(n + 1)]
    print(dfs(start, stand))