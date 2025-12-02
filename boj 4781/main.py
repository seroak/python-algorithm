import sys

input = sys.stdin.readline

while True:
    n, money = map(float, input().rstrip().rsplit())
    n = int(n)

    if n == 0 and money == 0.00:
        break

    money = int(money * 100)

    candies = []
    for _ in range(n):
        c, p = map(float, input().rstrip().rsplit())
        candies.append([int(c), int(p * 100 + 0.5)])

    # dp[i] = 돈이 i일때, 사탕 중 가장 높은 칼로리
    dp = [0] * 10001
    for i in range(n):
        for j in range(money+1):
            if candies[i][1] <= j:
                dp[j] = max(dp[j - candies[i][1]] + candies[i][0], dp[j])

    print(dp[money])
