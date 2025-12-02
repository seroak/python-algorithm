d, k = map(int, input().split())
dp = [[1, 0], [0, 1]]
for n in range(2, d):
    dp.append([dp[n-2][0]+dp[n-1][0], dp[n-2][1]+dp[n-1][1]])

for i in range(1, k):
    if (k - dp[d-1][0] * i) % dp[d-1][1] == 0:
        A = i
        B = (k - dp[d-1][0] * i) // dp[d-1][1]
        if A < B:
            print(A)
            print(B)
            exit(0)