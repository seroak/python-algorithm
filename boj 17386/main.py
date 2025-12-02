L1 = list(map(int, input().split()))
L2 = list(map(int, input().split()))


def ccw(x1, y1, x2, y2, x3, y3):
    return x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3


a = ccw(L1[0], L1[1], L1[2], L1[3], L2[0], L2[1])
b = ccw(L1[0], L1[1], L1[2], L1[3], L2[2], L2[3])

c = ccw(L2[0], L2[1], L2[2], L2[3], L1[0], L1[1])
d = ccw(L2[0], L2[1], L2[2], L2[3], L1[2], L1[3])

if a * b < 0 and c * d < 0:
    print(1)
else:
    print(0)
