t = int(input())
for _ in range(t):
    n = int(input())
    arr = list()
    for i in range(n):
        a, b = map(int, input().split())
        arr.append([a, b])
    arr.sort()
    count = 1
    mn = arr[0][1]
    for i in range(1, n):
        if mn > arr[i][1]:
            mn = arr[i][1]
            count += 1
    print(count)