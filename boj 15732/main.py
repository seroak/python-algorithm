n, k, d = map(int, input().split())
arr = []
for _ in range(k):
    tmp = list(map(int, input().split()))
    arr.append(tmp)


def count_nuts(mid):
    total = 0
    for a, b, c in arr:
        if mid < a:
            continue
        total += ((min(b, mid) - a) // c) + 1
        if total >= d:
            return total
    return total


left = 1
right = n

while left < right:
    mid = (left + right) // 2
    if count_nuts(mid) >= d:
        right = mid
    else:
        left = mid + 1
print(right)
