from collections import deque

n = int(input())
graph = [[] for _ in range(n + 1)]
indegree = [0 for _ in range(n + 1)]
cost = [0 for _ in range(n + 1)]

for i in range(n):
    tmp = list(map(int, input().split()))
    value = tmp[0]
    cost[i + 1] = value
    num = tmp[1]
    if num > 0:
        for k in tmp[2:]:
            graph[k].append(i + 1)
            indegree[i + 1] += 1

# DP 배열: 각 작업의 최소 완료 시간
dp = [0 for _ in range(n + 1)]

# 초기 위상 정렬 큐 생성
queue = deque()
for i in range(1, n + 1):
    if indegree[i] == 0:
        queue.append(i)
        dp[i] = cost[i]  # 초기 작업의 완료 시간은 작업 자체의 비용


while queue:
    curr = queue.popleft()
    for next_idx in graph[curr]:
        indegree[next_idx] -= 1
        dp[next_idx] = max(dp[next_idx], cost[next_idx] + dp[curr])
        if indegree[next_idx] == 0:
            queue.append(next_idx)

# 전체 작업의 완료 시간 중 최댓값이 정답
print(max(dp))
