n = int(input())
children = list()
for _ in range(n):
    children.append(int(input()))
dp = [1 for _ in range(n)]
for i in range(n):
    for j in range(i+1, n):
        if children[j] > children[i]:
            dp[j] = max(dp[j], dp[i] + 1)

mx = max(dp)
print(n - mx)