import sys

n, m = map(int, input().split())
arr = list()
arr.append(0)
for _ in range(n):
    tmp = int(input())
    arr.append(tmp)
tree = [0] * (n * 4)


def init(st, en, index):
    if st == en:
        tree[index] = arr[st]
        return arr[st]
    mid = (st + en) // 2
    tree[index] = min(init(st, mid, index * 2), init(mid + 1, en, index * 2 + 1))
    return tree[index]


def pick(st, en, index, left, right):
    if en < left or right < st:
        return sys.maxsize
    if left <= st and en <= right:
        return tree[index]
    mid = (st + en) // 2
    return min(pick(st, mid, index * 2, left, right), pick(mid + 1, en, index * 2 + 1, left, right))


init(1, n, 1)

for _ in range(m):
    a, b = map(int, input().split())
    print(pick(1, n, 1, a, b))
