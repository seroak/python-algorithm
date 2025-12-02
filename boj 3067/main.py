t = int(input())
for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    k = int(input())
    dp = [0 for _ in range(k + 1)]

    dp[0] = 1
    for coin in coins:
        for i in range(1, k+1):
            if i >= coin:
                dp[i] += dp[i-coin]
    print(dp[k])