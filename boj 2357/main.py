import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list()
tree = [[]] * (n * 4)
for _ in range(n):
    num = int(input())
    arr.append(num)


def init(start, end, index):
    if start == end:
        tree[index] = [arr[start], arr[start]]
        return [arr[start], arr[start]]
    mid = (start + end) // 2
    a = init(start, mid, index * 2)
    b = init(mid + 1, end, index * 2 + 1)

    tree[index] = [min(a[0], a[1], b[0], b[1]), max(a[0], a[1], b[0], b[1])]
    return tree[index]


def find(start, end, index, left, right):
    if start > right or end < left:
        return []
    if left <= start and end <= right:
        return [min(tree[index]), max(tree[index])]
    mid = (start + end) // 2
    tmp = find(start, mid, index * 2, left, right) + find(mid+1, end, index * 2 + 1, left, right)
    if len(tmp) == 0:
        return []
    else:
        return [min(tmp), max(tmp)]


init(0, len(arr) - 1, 1)

for _ in range(m):
    a, b = map(int, input().split())
    print(*find(0, len(arr) - 1, 1, a-1, b-1))
