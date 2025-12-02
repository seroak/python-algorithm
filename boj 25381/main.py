from collections import deque
arr = input()
answer = 0
queue = deque()

for i in range(len(arr)):
    if arr[i] == "B":
        queue.append(i)
    if arr[i] == "C":
        if queue:
            queue.popleft()
            answer += 1

for i in range(len(arr)):
    while queue and queue[0] <= i:
        queue.popleft()
    if arr[i] == "A" and queue:
        queue.popleft()
        answer += 1

print(answer)