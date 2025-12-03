t = int(input())
for _ in range(t):
    cost = int(input())
    k = len(str(cost))
    coins = [1, 10, 25]
    answer = 0
    dp =[10**15+1 for _ in range(100)]
    dp[0] = 0
    for c in [1, 10, 25]:
        for i in range(c, 100):
            dp[i] = min(dp[i], dp[i-c]+1)
    print(dp)
    while cost:
        print(cost)
        print(dp[cost%100])
        answer += dp[cost % 100]
        cost //= 100
    print(answer)