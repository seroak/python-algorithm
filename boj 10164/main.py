n, m, k = map(int, input().split())

# DP 테이블 초기화
dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
dp[1][1] = 1  # 시작점

# k가 없는 경우 (즉, 바로 끝까지 가는 경우)
if k == 0:
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    print(dp[n][m])
    exit(0)

# k의 좌표 계산 (1-based index로 조정)
x = (k - 1) // m + 1
y = (k - 1) % m + 1

# 첫 번째 구간 (시작점 -> k까지)
for i in range(1, x+1):
    for j in range(1, y+1):
        if i == 1 and j == 1:
            continue
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

# 두 번째 구간 (k -> 도착점까지)
for i in range(x, n+1):
    for j in range(y, m+1):
        if i == x and j == y:
            continue
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

# 정답 출력
print(dp[n][m])