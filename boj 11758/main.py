x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
a = x1 - x2
b = y1 - y2
c = x3 - x2
d = y3 - y2

ccw = (b * c) - (a * d)
if ccw < 0:
    print(-1)
elif ccw > 0:
    print(1)
else:
    print(0)