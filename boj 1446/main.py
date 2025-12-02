n, d = map(int, input().split())
ally = dict()
for _ in range(n):
    st, en, dist = map(int, input().split())
    if st > d or en > d:
        continue
    if st not in ally:
        ally[st] = list()
    ally[st].append([en, dist])

dp = [float('inf') for _ in range(d+1)]
dp[0] = 0
for i in range(d):
    if i in ally:
        for en, dist in ally[i]:
            dp[en] = min(dp[en], dp[i] + dist)
    dp[i+1] = min(dp[i+1], dp[i] + 1)
print(dp[-1])
