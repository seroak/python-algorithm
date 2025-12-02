import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n = int(input())
population = list(map(int, input().split()))
population = [0] + population
dp = [[0, 0] for _ in range(n+1)]
for i in range(1, n+1):
    dp[i][0] = population[i]
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False for _ in range(n+1)]
def dfs(cur):
    visited[cur] = True
    for i in graph[cur]:
        if visited[i] is True:
            continue
        # 우수 마을 선정, 우수 마을 선정 안됨
        good, bad = dfs(i)
        # 우수 마을이 선정되면 자식은 무조건 우수 마을 선정을 하면 안됨
        dp[cur][0] += bad
        # 우수 마을이 선정이 안되면 자식은 우수마을이 선정되고 되고 안돼도 됨
        dp[cur][1] += max(good, bad)

    return dp[cur][0], dp[cur][1]
dfs(1)
print(dp)
print(max(dp[1]))