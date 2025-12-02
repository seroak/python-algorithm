import sys

input = sys.stdin.readline

n, m = map(int, input().split())  # n<=100
dont_ent = list(map(int, input().split()))
inf = sys.maxsize

dp = [[inf for _ in range(45)] for _ in range(106)]

dp[0][0] = 0
for i in range(n + 1):
    for j in range(40):
        if dp[i][j] == inf:
            continue
        result = dp[i][j]

        # 리조트 방문 x
        if i + 1 in dont_ent:
            dp[i + 1][j] = min(dp[i + 1][j], result)
        # 쿠폰 사용
        if j >= 3:
            dp[i + 1][j - 3] = min(dp[i + 1][j - 3], result)
        # 하루 이용권
        dp[i + 1][j] = min(dp[i + 1][j], result + 10000)
        # 3일 이용권
        for k in range(1, 4):
            dp[i + k][j + 1] = min(dp[i + k][j + 1], result + 25000)

        # 5일 이용권
        for k in range(1, 6):
            dp[i + k][j + 2] = min(dp[i + k][j + 2], result + 37000)
print(min(dp[n]))
