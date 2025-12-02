from collections import deque
def a_button(n):
    n += 1
    return n


def b_button(n):
    if n == 0:
        return 0
    n *= 2
    if n > 99999:
        return inf
    n = str(n)
    if int(n[0]) > 1:
        length = len(n)
        n = int(n)
        n -= 10 ** (length-1)
        return n
    else:

        return int(n[1:])


n, t, g = map(int, input().split())
inf = float("inf")
arr = [inf] * 100000
queue = deque()
queue.append((n, 0))
arr[n] = 0
while queue:
    cur, count = queue.popleft()
    if count > t:
        continue

    if cur == g:
        print(count)
        break
    a = a_button(cur)
    if a <= 99999:
        if arr[a] > count + arr[cur]:
            arr[a] = count + 1
            queue.append((a, count + 1))
    b = b_button(cur)
    if b <= 99999:
        if arr[b] > count + arr[cur]:
            arr[b] = count + 1
            queue.append((b, count + 1))
else:
    print('ANG')