n, k = map(int, input().split())
dp = [0 for _ in range(k + 1)]
numbers = list()
for i in range(n):
    num = int(input())
    numbers.append(num)
dp[0] = 1
for num in numbers:
    for i in range(1, k+1):
        if i >= num:
            dp[i] = dp[i] + dp[i-num]
print(dp[k])