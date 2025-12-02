def solution(strs, t):
    n = len(t)
    INF = float("inf")
    dp = [INF] * n + [0]
    for i in range(n - 1, -1, -1):
        for j in range(1, min(6, n - i + 1)):
            if t[i:i+j] in strs:
               dp[i] = min(dp[i], dp[i+j] + 1)
    return -1 if dp[0] == INF else dp[0]


strs = ["ba", "na", "n", "a"]
t = "banana"
solution(strs, t)
