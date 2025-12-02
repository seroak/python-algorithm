n = int(input())
weight = list(map(int, input().split()))
weight = [0] + weight
graph = list([] for _ in range(n + 1))
# dp[현재 노드를 선택했을 때 , 현재 노드를 선택하지 않았을 때]
dp = [[0, 0] for _ in range(n + 1)]
dp_set = [[set(),set()]for _ in range(n+1)]
for i in range(1, n+1):
    dp[i][0] = weight[i]
    dp_set[i][0].add(i)

visited = [False for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(cur):
    visited[cur] = True
    for i in graph[cur]:
        if visited[i] is False:
            select, not_select = dfs(i)
            dp[cur][0] += not_select
            dp_set[cur][0] = dp_set[cur][0] | dp_set[i][1]
            if select > not_select:
                dp[cur][1] += select
                dp_set[cur][1] = dp_set[cur][1] | dp_set[i][0]
            else:
                dp[cur][1] += not_select
                dp_set[cur][1] = dp_set[cur][1] | dp_set[i][1]
    return dp[cur][0], dp[cur][1]
dfs(1)
mx = max(dp[1])
index = dp[1].index(mx)
print(mx)
print(*sorted(list(dp_set[1][index])))
