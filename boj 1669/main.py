import math

x, y = map(int, input().split())
diff = y - x  # 차이
n = int(math.sqrt(diff))

if x == y:
    print(0)
else:
    if diff == (n**2):
        print((2 * n) - 1)
    else:
        if diff <= n ** 2 + n:
            print(2 * n)
        else:
            print((2 * n) + 1)
