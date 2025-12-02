from collections import deque

t = int(input())
d = [60, 10, -10, 1, -1]
for _ in range(t):
    n = int(input())
    count = n // 60
    target = n % 60
    start = [count, 0, 0, 0, 0]
    queue = deque([(0, start)])
    visited = [False for _ in range(61)]
    answer = None
    while queue:
        size = len(queue)

        for _ in range(size):
            cnt, cur = queue.popleft()
            visited[cnt] = True
            if cnt == target:
                if answer is None:
                    answer = cur
                else:
                    for i in range(5):
                        if answer[i] > cur[i]:
                            answer = cur
                            break
                        elif answer[i] < cur[i]:
                            break
            for i in range(5):
                if 0 < cnt + d[i] <= 60:
                    if visited[cnt + d[i]] is False:
                        tmp = cur[:]
                        tmp[i] += 1

                        queue.append((cnt + d[i], tmp))
    print(*answer)