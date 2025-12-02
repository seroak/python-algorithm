from collections import deque

t = int(input())
for _ in range(t):
    queue = deque()
    visited = [False for _ in range(10000)]
    tmp = list(map(int, input().split()))
    queue.append(["", tmp[0]])
    while queue:
        order, num = queue.popleft()
        if num == tmp[1]:
            print(order)
            break
        # D
        D = (num * 2) % 10000
        # S
        S = (num - 1) % 10000
        # L
        L = num % 1000 * 10 + num // 1000
        # R
        R = num % 10 * 1000 + num // 10
        if visited[D] is False:
            visited[D] = True
            queue.append([order + "D", D])
        if visited[S] is False:
            visited[S] = True
            queue.append([order + "S", S])
        if visited[L] is False:
            visited[L] = True
            queue.append([order + "L", L])
        if visited[R] is False:
            visited[R] = True
            queue.append([order + "R", R])
