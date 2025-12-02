import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))


def solve(arr):
    total = sum(arr)
    # 쪽방이 하나도 없다면 n//2이다
    if total == 0:
        return n // 2
    idx = 0
    # 시작점이 쪽방이 없는 곳에 시작하면 최적의 값을 못찾을 수 있어서 쪽방이 있는 곳부터 시작해야한다
    for idx, a in enumerate(arr):
        if a:
            break
    arr = arr[idx:] + arr[:idx]
    arr.append(arr[0])
    chk = [0] * (n+1)

    for i in range(1,n):
        if arr[i] == 0:
            if chk[i-1] == 0 and chk[i+1] == 0:
                total += 1
                chk[i] = 1

    return total


print(solve(arr))
