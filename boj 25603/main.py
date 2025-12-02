import sys

input = sys.stdin.readline

N, K = map(int, input().split())
costs = list(map(int, input().split()))


def check(limit):
    combo = 0
    for i in costs:
        if i <= limit:
            combo = 0
        else:
            combo += 1
        if combo >= K:
            return False
    return True


left = 0
right = 1000000000
while left < right:
    mid = (left + right) // 2
    if check(mid):
        right = mid
    else:
        left = mid + 1
print(left)
