import sys
# 남아있는 성냥개비에서 [0]은 최소 [-1]은 최대이다 하지만 1의자리에서는 6[0]은 6이다
dp = [sys.maxsize for i in range(101)]
dp[2], dp[3], dp[4], dp[5], dp[6], dp[7] = 1, 7, 4, 2, 6, 8

min_num = [0, 0, 1, 7, 4, 2, 0, 8]
for i in range(8, 101):
    for j in range(2, 8):
        dp[i] = min(dp[i], dp[i-j]*10 + min_num[j])
print(dp)
t = int(input())
for i in range(t):
    num = int(input())
    # 큰 수
    if num % 2 == 1:
        big = ((num // 2) - 1) * "1"
        big = "7" + big
    else:
        big = (num // 2) * "1"

    # 작은 수
    # 작은 수가 1의 자리로 해결이 가능할 때
    print(dp[num], big)


