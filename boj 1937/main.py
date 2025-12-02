from sys import stdin
input = stdin.readline

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)


def dfs(r, c):
    if check[r][c]:  # 방문한 적이 있다면 해당 값을 그대로 가져다 사용
        return check[r][c]

    check[r][c] = 1  # 첫 방문 시 해당 위치는 무조건 먹을 수 있으므로 1
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if not (0 <= nr < N and 0 <= nc < N):
            continue

        if A[r][c] < A[nr][nc]:  # 이동할 곳에 대나무가 더 많다면
            # 판다가 오래 사는 일수 = 4방향 중 판다가 가장 많이 이동한 횟수(최장 경로) + 1
            check[r][c] = max(check[r][c], dfs(nr, nc) + 1)
    return check[r][c]

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
check = [[0] * N for _ in range(N)]     # DP Table(for memoization)

for r in range(N):
    for c in range(N):
        if not check[r][c]:		# 첫 방문이 아닌 경우에만 dfs 실행
            dfs(r, c)
MAX = 0
for i in range(N):
    MAX = max(MAX, max(check[i]))
print(MAX)