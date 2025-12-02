s = str(input())
t = str(input())
dp = [[0 for _ in range(len(s) + 1)] for _ in range(len(t) + 1)]
for i in range(1, len(t) + 1):
    for j in range(1, len(s) + 1):
        if t[i - 1] == s[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
answer = 0
for i in dp:
    for j in i:
        answer = max(answer, j)
print(answer)
