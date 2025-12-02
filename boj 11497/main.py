t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    tmp = list()
    for i in range(0, n, 2):
        tmp.append(arr[i])
    tmp2 = list()
    for i in range(1, n, 2):
        tmp2.append(arr[i])
    for i in range(len(tmp2) - 1, -1, -1):
        tmp.append(tmp2[i])

    mx = 0
    for i in range(len(tmp) - 1):
        minuse = abs(tmp[i] - tmp[i + 1])
        mx = max(mx, minuse)
    print(mx)
