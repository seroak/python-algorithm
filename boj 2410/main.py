n = int(input())
dp = [0 for _ in range(n + 1)]
numbers = list()
q = 1
tmp = 1
while tmp <= n:
    numbers.append(tmp)
    tmp = 2 ** q
    q += 1

dp[0] = 1
for num in numbers:
    for i in range(1, n+1):
        if i >= num:
            dp[i] = (dp[i-num] + dp[i]) % 1000000000
print(dp[n])