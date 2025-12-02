n, m = map(int, input().split())
arr = []
for i in range(n):
    s, l = map(int, input().split())
    if s > l:
        arr.append([l, s])
arr.sort(lambda.)