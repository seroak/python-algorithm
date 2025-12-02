from collections import deque

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    house = list(map(int, input().split()))
    house = house[:] + house[:]

    queue = deque()
    acc = 0
    answer = 0
    for i in range(m):
        queue.append(house[i])
        acc += house[i]
    if acc < k:
        answer += 1
    if n != m:
        for i in range(m, n + m - 1):
            num = queue.popleft()
            acc -= num
            queue.append(house[i])
            acc += house[i]
            if acc < k:
                answer += 1

    print(answer)