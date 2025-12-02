n, k = map(int, input().split())
bag = [list(map(int, input().split())) for _ in range(n)]

dp = [[0 for _ in range(n+1)] for _ in range(k+1)]
for i in range(1, n+1):
    for j in range(1, k+1):
        if j >= bag[i-1][0]: # 가방에 해당 물건을 넣을 수 있는 경우
            # dp에 바로 위에 무게를 빼고 새로운 물건을 담았을 때 가치 vs 새로운 물건을 안담고 그대로 가는 경우
            dp[i][j] = max(dp[i-1][j-bag[i-1][0]]+bag[i-1][1], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
print(dp)