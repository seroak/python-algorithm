n, m = map(int, input().split())
v = [[0] * m]
for _ in range(n):
    tmp = list(map(int, input().split()))
    v.append(tmp[1:])

dp = [[0] * 2 for _ in range(n + 1)]
for i in range(n + 1):
    dp[i][0] = v[i][0]

ans = [[0] * m for _ in range(n + 1)]
for i in range(n + 1):
    ans[i][0] = i
for company in range(1, m):
    for total_money in range(n + 1):
        for invest in range(total_money + 1):
            # 현재 회사에 투자할 돈과 그 나머지 돈을 분배하는 모든 경우의 수를 탐색
            # print(total_money-invest, company, invest)
            profit = dp[total_money - invest][0] + v[invest][company]
            if profit > dp[total_money][1]:

                dp[total_money][1] = profit
                ans[total_money][company] = invest
    for i in range(n + 1):
        dp[i][0] = dp[i][1]
        dp[i][1] = 0

print(dp[n][0])

num = n
idx = m - 1
arr = []
while idx >= 0:
    arr.append(ans[num][idx])
    num -= ans[num][idx]
    idx -= 1
arr.reverse()
print(" ".join(map(str, arr)))