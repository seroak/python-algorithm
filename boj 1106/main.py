# C = 늘려야하는 목표 고객 수 N = 형택이가 홍보할 수 있는 도시의 수
C, N = map(int, input().split())
hotel = [[0, 0]]

maxCost = float("INF")
for i in range(N):
    tmp = list(map(int, input().split()))
    hotel.append(tmp)
dp = [[maxCost for _ in range(C + 1)] for _ in range(N + 1)]
for i in range(1,N+1):

    for j in range(1, C+1):
        k = 0
        cost = hotel[i][0]
        benefit = hotel[i][1]
        dp[i][j] = dp[i - 1][j]
        while True:
            if j - benefit * k <= 0:
                dp[i][j] = min(dp[i][j], cost * k)
                break
            else:
                dp[i][j] = min(dp[i][j],  dp[i][j - benefit * k] + cost * k)
                k += 1

print(dp[-1][-1])

