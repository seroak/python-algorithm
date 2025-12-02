import sys
input = sys.stdin.readline
string = list(map(int, input().rstrip()))
n = len(string)
dp = [0 for _ in range(n+1)]
dp[0] = 1
for i in range(1, n+1):
    if i >= 2:
        if 10 <= (string[i-2] * 10) + string[i-1] <= 34:
            dp[i] += dp[i-2]
    if string[i-1] != 0:
        dp[i] += dp[i-1]
print(dp[-1])