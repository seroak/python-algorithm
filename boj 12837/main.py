n, m = map(int, input().split())
tree = [0] * ((4 * n) + 1)
arr = [0] * (n + 1)


def update(left, right, index, target):
    if left == target and right == target:
        tree[index] = arr[target]
        return tree[index]
    if right < target or left > target:
        return tree[index]
    mid = (left + right) // 2
    result1 = update(left, mid, 2 * index, target)
    result2 = update(mid + 1, right, (2 * index) + 1, target)
    tree[index] = result1 + result2
    return tree[index]


def sum_tree(left, right, st, en, index):
    if en < left or right < st:
        return 0
    if st <= left and right <= en:
        return tree[index]
    mid = (left + right) // 2
    result1 = sum_tree(left, mid, st, en, 2 * index)
    result2 = sum_tree(mid + 1, right, st, en, 2 * index + 1)
    return result1 + result2


for _ in range(m):
    query, p, q = map(int, input().split())
    if query == 1:
        arr[p] += q
        update(1, n, 1, p)
    if query == 2:
        print(sum_tree(1, n, p, q, 1))
