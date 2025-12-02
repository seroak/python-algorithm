import math
t = int(input())
for _ in range(t):
    n, m, x, y = map(int, input().split())
    if n > m:
        n, m = m, n
        x, y = y, x
    lcm_nm = (n * m) // math.gcd(n, m)  # 최소공배수(LCM) 계산
    tmp = x
    for i in range(lcm_nm // n):
        tmp = (tmp + n) % m
        if tmp == y:
            print((i+1) * n + x)
            break
    else:
        print(-1)
