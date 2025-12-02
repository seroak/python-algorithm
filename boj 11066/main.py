import math


def solve():
    n = int(input())
    arr = [int(x) for x in input().split()]
    rst = [[0 for _ in range(n)] for _ in range(n)]

    for j in range(1, n):
        for i in range(j - 1, -1, -1):
            sm = math.inf
            for k in range(j - i):
                sm = min(sm, rst[i][i + k] + rst[i + 1 + k][j])
            rst[i][j] = sum(arr[i:j+1]) + sm
    print(rst[0][-1])
t = int(input())
for _ in range(t):
    solve()
