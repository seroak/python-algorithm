n, q = map(int, input().split())
arr = list(map(int, input().split()))
tree = [0] * (n * 4)


def init(st, en, index):
    if st == en:
        tree[index] = arr[st]
        return arr[st]
    mid = (st + en) // 2
    tree[index] = init(st, mid, index * 2) + init(mid + 1, en, index * 2 + 1)
    return tree[index]


def sum_tree(st, en, index, left, right):
    if en < left or right < st:
        return 0
    if left <= st and en <= right:
        return tree[index]
    mid = (st + en) // 2
    return sum_tree(st, mid, index * 2, left, right) + sum_tree(mid + 1, en, index * 2 + 1, left, right)

def change_tree(st, en, index, num):
    if num < st or en < num:
        return tree[index]
    if st == num and en == num:
        tree[index] = arr[num]
        return tree[index]
    mid = (st + en) // 2
    tree[index] = change_tree(st, mid, index * 2, num) + change_tree(mid + 1, en, index * 2 + 1, num)
    return tree[index]

init(0, n - 1, 1)

for _ in range(q):
    x, y, a, b = map(int, input().split())
    small = min(x, y)
    big = max(x, y)
    print(sum_tree(0, n-1, 1, small-1, big-1))
    arr[a-1] = b
    change_tree(0, n-1, 1, a-1)
