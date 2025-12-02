n, s = map(int, input().split())
v = [(0, 0)]
for _ in range(n):
    h, c = map(int, input().split())
    v.append((h, c))

v.sort()
lim = [0] * (n+1)
dp = [0] * (n+1)
for i in range(1, n+1):
    lim[i] = lim[i-1]
    while lim[i] < i and v[i][0] - v[lim[i]][0] >= s:
        lim[i] += 1
    lim[i] -= 1
for i in range(1, n+1):
    dp[i] = max(dp[i-1], dp[lim[i]] + v[i][1])
print(dp[n])