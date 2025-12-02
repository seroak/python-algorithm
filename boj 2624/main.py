T = int(input())
K = int(input())
dp = [0] * (T+1)
dp[0] = 1

for _ in range(K):
    penny, penny_cnt = map(int, input().split())

    for i in range(T, -1, -1):
        j = 1
        while j <= penny_cnt and i - penny * j >= 0:
            dp[i] += dp[i - penny * j]
            j += 1

print(dp[T])