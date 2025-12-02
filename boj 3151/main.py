import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort()


def lower_bound(right, num):
    st = right
    en = n
    while st < en:
        mid = (en + st) // 2
        if arr[mid] < num:
            st = mid + 1
        else:
            en = mid
    return st


def upper_bound(right, num):
    st = right
    en = n
    while st < en:
        mid = (en + st) // 2
        if arr[mid] <= num:
            st = mid + 1
        else:
            en = mid
    return st


ans = 0

for i in range(n - 2):
    for j in range(i + 1, n-1):

        num = arr[j] + arr[i]
        left = lower_bound(j+1, -num)
        right = upper_bound(j+1, -num)

        ans += right - left
print(ans)
