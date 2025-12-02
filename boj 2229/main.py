import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(i - 1, -1, -1):
        print(j, i)
        dp[i] = max(dp[i], dp[j] + abs(max(arr[j:i]) - min(arr[j:i])))

print(dp)
