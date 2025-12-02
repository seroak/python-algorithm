from collections import deque

n, w, l = map(int, input().split())
queue = deque()
for _ in range(w):
    queue.append(0)
truck = list(map(int, input().split()))
count = n
idx = 0
weight = 0
time = 0
while count:

    num = queue.popleft()
    if num != 0:
        count -= 1
        weight -= num
    if idx < n and weight + truck[idx] <= l:
        queue.append(truck[idx])
        weight += truck[idx]
        idx += 1

    else:
        queue.append(0)
    time += 1
print(time)
