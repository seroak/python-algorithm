n, m, k = map(int, input().split())
arr = list()
arr.append(0)
for i in range(n):
    num = int(input())
    arr.append(num)
tree = [0] * (4 * n)


def init(st, en, index):
    if st == en:
        tree[index] = arr[st]
        return arr[st]
    mid = (st + en) // 2
    tree[index] = (init(st, mid, index * 2) * init(mid + 1, en, index * 2 + 1)) % 1000000007
    return tree[index]


def change(st, en, index, target):
    if target < st or target > en:
        return tree[index]
    if st == target and en == target:
        tree[index] = arr[st]
        return arr[st]
    mid = (st + en) // 2
    tree[index] = (change(st, mid, index * 2, target) * change(mid + 1, en, index * 2 + 1, target)) % 1000000007
    return tree[index]


def mul(st, en, index, left, right):
    if en < left or right < st:
        return 1
    if left <= st and en <= right:
        return tree[index]
    mid = (st + en) // 2
    return (mul(st, mid, index * 2, left, right) * mul(mid + 1, en, index * 2 + 1, left, right)) % 1000000007


init(1, n, 1)

for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        arr[b] = c
        change(1, n, 1, b)
    if a == 2:
        print(mul(1, n, 1, b, c))
