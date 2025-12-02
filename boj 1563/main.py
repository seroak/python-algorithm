n = int(input())
dp = [[[0 for _ in range(4)] for _ in range(3)] for _ in range(n)]
# 지각 2회  결석 3회는 누적하지 않는다
dp[0][0][0] = 1
dp[0][1][0] = 1
dp[0][0][1] = 1
for k in range(n - 1):
    for i in range(3):
        for j in range(4):
            if dp[k][i][j] == 0:
                continue
            # 지각을 했을 때
            # 지각 2회 결석 3회 누적 x
            if i + 1 < 2 and j < 3:
                dp[k + 1][i + 1][0] = (dp[k + 1][i + 1][0] + dp[k][i][j]) % 1000000
            # 결석을 했을때
            # 지각 2회 결석 3회 누적 x
            if i < 2 and j + 1 < 3:
                dp[k + 1][i][j + 1] = (dp[k + 1][i][j + 1] + dp[k][i][j]) % 1000000
            # 출석을 했을때
            if i < 2 and j < 3:
                dp[k + 1][i][0] = (dp[k + 1][i][0] + dp[k][i][j]) % 1000000

ans = 0
for i in dp[-1]:
    for j in i:
        ans = (ans + j) % 1000000
print(ans % 1000000)
