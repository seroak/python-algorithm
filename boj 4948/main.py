import math
dp = [True for _ in range(250000)]
dp[0] = False
dp[1] = False
for i in range(2, int(math.sqrt(250000)) + 1):
    if dp[i] is True:
        j = 2
        while i * j < 250000:
            dp[i * j] = False
            j += 1

acc_sum = list()
count = 0
for i in dp:
    if i is True:
        count += 1
    acc_sum.append(count)

while True:
    num = int(input())
    if num == 0:
        break
    print(acc_sum[2*num] - acc_sum[num])