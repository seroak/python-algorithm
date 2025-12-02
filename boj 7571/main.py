n, m = map(int, input().split())
r = []
c = []
arr = []
for _ in range(m):
    a, b = map(int, input().split())
    r.append(a)
    c.append(b)
    arr.append([a, b])

r.sort()
c.sort()
mid_r = r[m//2]
mid_c = c[m//2]
answer = 0
for i in range(m):
    a, b = arr[i]
    answer += abs(mid_r - a)
    answer += abs(mid_c - b)
print(answer)