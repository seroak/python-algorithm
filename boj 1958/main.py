string1 = input()
string2 = input()
string3 = input()
dp = [[[0 for _ in range(len(string1) + 1)] for _ in range(len(string2) + 1)] for _ in range(len(string3) + 1)]
for i in range(1, len(string1) + 1):
    for j in range(1, len(string2) + 1):
        for k in range(1, len(string3) + 1):
            if string1[i - 1] == string2[j - 1] == string3[k - 1]:
                dp[k][j][i] = dp[k - 1][j - 1][i - 1] + 1
            else:
                dp[k][j][i] = max(dp[k - 1][j][i], dp[k][j - 1][i], dp[k][j][i - 1])
print(dp[-1][-1][-1])
