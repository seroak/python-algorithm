n = int(input())

arr = list()


def hanoi(num, start, to, via):
    if num == 1:
        arr.append((start, to))
        return

    hanoi(num - 1, start, via, to)
    arr.append((start, to))
    hanoi(num - 1, via, to, start)


def hanoi2(num, start, to, via):
    global cnt
    if num == 1:
        cnt += 1
        return

    hanoi2(num - 1, start, via, to)
    cnt += 1
    hanoi2(num - 1, via, to, start)


if n <= 20:
    hanoi(n, 1, 3, 2)
    print(len(arr))
    for st, en in arr:
        print(st, en)
else:
    cnt = 0
    hanoi2(n, 1, 3, 2)
    print(cnt)
