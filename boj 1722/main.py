import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
cache = {}


def find_factorial(n):
    if n in cache:
        return cache[n]
    # 원칙상 1이 나오면 1을 반환하고 0이 들어올일이 없긴한데 나중에 확인할것 이렇게 하면 틀림
    if n <= 1:
        return 1
    cache[n] = n * find_factorial(n - 1)
    return cache[n]


if data[0] == 1:
    k = data[1]
    arr = [i for i in range(1, n + 1)]
    ans = list()
    for i in range(n):

        x = find_factorial(n - 1 - i)
        step = (k - 1) // x
        ans.append(arr[step])
        arr.remove(arr[step])
        k -= step * x
    print(*ans)
else:
    arr = data[1:]
    sorted_arr = sorted(arr)
    ans = 1
    for i in range(n):
        x = find_factorial(n-i-1)
        step = sorted_arr.index(arr[i])
        sorted_arr.remove(arr[i])
        ans += x * step
    print(ans)
