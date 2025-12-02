n, m, k = map(int, input().split())
arr = list()

for i in range(n):
    num = int(input())
    arr.append(num)
tree = [0] * (len(arr) * 4)


def init(st, en, index):
    if st == en:
        tree[index] = arr[st]
        return tree[index]
    mid = (st + en) // 2
    tree[index] = init(st, mid, index * 2) + init(mid + 1, en, (index * 2) + 1)
    return tree[index]


def interval_sum(st, en, index, left, right):
    # 범위를 벗어났을 때
    if right < st or left > en:
        return 0
    if left <= st and en <= right:
        return tree[index]
    mid = (st + en) // 2

    return interval_sum(st, mid, index * 2, left, right) + interval_sum(mid + 1, en, index * 2 + 1, left, right)


def update(start, end, index, what, value):
    if what < start or what > end:
        return
    tree[index] += value
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, index * 2, what, value)
    update(mid + 1, end, index * 2 + 1, what, value)


init(0, len(arr) - 1, 1)
for i in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        value = c - arr[b - 1]
        arr[b - 1] = c  # 값을 먼저 갱신
        update(0, len(arr) - 1, 1, b - 1, value)

    if a == 2:
        print(interval_sum(0, len(arr) - 1, 1, b-1, c-1))

