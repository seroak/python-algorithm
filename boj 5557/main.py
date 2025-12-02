# dp[i][j] i번쨰 수를 이용해서 j 가 될 수 있는 경우의 수
n = int(input())
arr = list(map(int, input().split()))
dp = [[0] * 21 for _ in range(n-1)]
dp[0][arr[0]] = 1
for i in range(n-2):
    for j in range(21):
        if dp[i][j] != 0:
            # 더할 수 있는 경우
            if j + arr[i+1] <= 20:

                dp[i+1][j + arr[i+1]] += dp[i][j]
            # 뺄 수 있는 경우
            if j - arr[i+1] >= 0:
                dp[i+1][j - arr[i+1]] += dp[i][j]

print(dp[-1][arr[-1]])
