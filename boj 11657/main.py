n, m = map(int, input().split())
graph = []
for _ in range(m):
    node = list(map(int, input().split()))
    graph.append(node)
INF = float("inf")
dist = [INF] * (n + 1)

def bf(start):
    dist[start] = 0
    for i in range(n):
        for j in range(m):
            cur, next, cost = graph[j]
            if dist[cur] != INF and dist[next] > dist[cur] + cost:
                dist[next] = dist[cur] + cost
                if i == n-1:
                    return True
    return False

if bf(1):
    print(-1)
    exit(0)
for i in dist[2:]:
    if i == INF:
        print(-1)
    else:
        print(i)
