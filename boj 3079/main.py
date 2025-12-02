import sys
n, m = map(int, input().split())
test = list()
for _ in range(n):
    num = int(input())
    test.append(num)

st = 0
en = sys.maxsize
while st < en:
    mid = (st + en) // 2
    res = 0
    for i in test:
        res += mid // i
    if res < m:
        st = mid + 1
    else:
        en = mid
print(st)