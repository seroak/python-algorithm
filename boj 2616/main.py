n = int(input())
train = list(map(int, input().split()))
m = int(input())
dp = [[0 for _ in range(n + 1)] for _ in range(4)]
sum_train = list()
tmp = 0
for i in range(len(train)):
    tmp += train[i]
    sum_train.append(tmp)

sum_train = [0] + sum_train
for i in range(1, 4):
    for j in range(n + 1):
        if i * m <= j:
            dp[i][j] = max(sum_train[j] - sum_train[j - m] + dp[i - 1][j - m], dp[i][j - 1])
print(dp[3][n])
