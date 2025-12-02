mn, mx = map(int, input().split())
dp = [False] * (mx - mn + 1)
count = mx - mn + 1
# 몇까지 거듭제곱을 홗인해야 하나 2부터 mx의 루트까지만 확인하면 된다 그 이상은 mx를 넘어간다
for i in range(2, int(mx ** 0.5) + 1):
    square = i ** 2
    # mn과 가장 가까운 배수를 구한다
    for j in range((((mn - 1) // square) + 1) * square, mx + 1, square):
        if dp[j - mn] is False:
            dp[j - mn] = True
            count -= 1

print(count)
