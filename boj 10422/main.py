t = int(input())
dp = [0 for _ in range(2501)]
dp[0] = 1
dp[1] = 1
dp[2] = 2
for i in range(3, 2501):
    for j in range(1, i+1):
        dp[i] += (dp[i-j] * dp[j-1]) % 1000000007
        dp[i] = dp[i] % 1000000007

for _ in range(t):
    a = int(input())
    if a % 2 == 1:
        print(0)
        continue
    a = a//2
    print(dp[a])