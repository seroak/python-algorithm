import sys
input = sys.stdin.readline
n, m = map(int, input().split())
tree = [0] * (n * 4)
arr = [0 for _ in range(n+1)]


def sum_tree(st, en, index, left, right):
    if en < left or right < st:
        return 0
    if left <= st and en <= right:
        return tree[index]
    mid = (st + en) // 2
    return sum_tree(st, mid, index * 2, left, right) + sum_tree(mid + 1, en, index * 2 + 1, left, right)


def modify_tree(st, en, index, target):
    if target < st or en < target:
        return tree[index]
    if st == target and en == target:
        tree[index] = arr[target]
        return tree[index]
    mid = (st + en) // 2
    tree[index] = modify_tree(st, mid, index * 2, target) + modify_tree(mid + 1, en, index * 2 + 1, target)
    return tree[index]


for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 0:
        if c < b:
            b, c = c, b
        print(sum_tree(0, n, 1, b, c))
    elif a == 1:
        arr[b] = c
        modify_tree(0, n, 1, b)
