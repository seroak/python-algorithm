n, k = map(int, input().split())
student = list(map(int, input().split()))
pre_fix = list()
pre = 0
pre_fix.append(0)
for i in student:
    pre += i
    pre_fix.append(pre)

for _ in range(k):
    a, b = map(int, input().split())
    print("%0.2f" % float((pre_fix[b] - pre_fix[a - 1]) / (b - a + 1)))
