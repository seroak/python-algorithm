n = int(input())
arr = list(map(int, input().split()))
dp = [0 for _ in range(n)]
dp[0] = 1
answer = 0
for i in range(1, n):
    mx = 0
    for j in range(i-1, -1, -1):
        if arr[i] > arr[j]:
            mx = max(dp[j], mx)
    dp[i] = mx + 1
    answer = max(dp[i], answer)

print(answer)