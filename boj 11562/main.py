n, m = map(int, input().split())
inf = float("inf")
arr = [[inf] * n for _ in range(n)]
for i in range(n):
    arr[i][i] = 0
for _ in range(m):
    u, v, b = map(int, input().split())
    u = u - 1
    v = v - 1
    if b == 0:
        arr[u][v] = 0
        arr[v][u] = 1
    else:
        arr[u][v] = 0
        arr[v][u] = 0
for k in range(n):
    for i in range(n):
        for j in range(n):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

k = int(input())
for i in range(k):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    print(arr[a][b])