from collections import deque


def is_sorted(arr):
    return all(int(arr[i]) <= int(arr[i + 1]) for i in range(len(arr) - 1))


n = int(input())
numbers = input().split()
m = int(input())

controls = [tuple(map(int, input().split())) for _ in range(m)]

queue = deque()
visited = {}

start = "".join(numbers)
queue.append((numbers, 0))
visited[start] = 0
mn = float("inf")

while queue:
    num, cnt = queue.popleft()

    if is_sorted(num):
        mn = min(mn, cnt)
        continue

    for a, b, c in controls:
        tmp_num = num[:]
        tmp_num[a - 1], tmp_num[b - 1] = tmp_num[b - 1], tmp_num[a - 1]
        new_cnt = cnt + c
        key = "".join(tmp_num)

        if key not in visited or new_cnt < visited[key]:
            visited[key] = new_cnt
            queue.append((tmp_num, new_cnt))

print(-1 if mn == float("inf") else mn)
