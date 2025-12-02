n = int(input())
arr = list(map(int, input().split()))
dp = [0 for _ in range(n + 1)]
mx = 0
for i in range(n):
    current = arr[i]
    dp[current] = dp[current - 1] + 1
mx_lin = max(dp)
print(n - mx_lin)
