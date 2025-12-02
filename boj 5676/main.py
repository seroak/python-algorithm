import sys


def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    return 0


def init(st, en, index):
    if st == en:
        tree[index] = sign(arr[st])
        return tree[index]
    mid = (st + en) // 2
    tree[index] = init(st, mid, index * 2) * init(mid + 1, en, index * 2 + 1)
    return tree[index]


def multiple(st, en, index, left, right):
    if en < left or right < st:
        return 1
    if left <= st and en <= right:
        return tree[index]
    mid = (st + en) // 2
    return multiple(st, mid, index * 2, left, right) * multiple(mid + 1, en, index * 2 + 1, left, right)


def change(st, en, index, target):
    if target < st or en < target:
        return tree[index]
    if st == target and en == target:
        tree[index] = sign(arr[target])
        return tree[index]
    mid = (st + en) // 2
    tree[index] = change(st, mid, index * 2, target) * change(mid + 1, en, index * 2 + 1, target)
    return tree[index]


def solve():
    n, k = map(int, sys.stdin.readline().split())
    global arr, tree
    arr = list(map(int, sys.stdin.readline().split()))
    tree = [0 for _ in range(4 * n)]

    init(0, n - 1, 1)

    result = []
    for _ in range(k):
        command = sys.stdin.readline().split()
        if command[0] == "C":
            i, v = int(command[1]) - 1, int(command[2])
            arr[i] = v
            change(0, n - 1, 1, i)
        elif command[0] == "P":
            i, j = int(command[1]) - 1, int(command[2]) - 1
            num = multiple(0, n - 1, 1, i, j)
            if num > 0:
                result.append("+")
            elif num < 0:
                result.append("-")
            else:
                result.append("0")

    print("".join(result))


if __name__ == "__main__":
    try:
        while True:
            solve()
    except:
        pass