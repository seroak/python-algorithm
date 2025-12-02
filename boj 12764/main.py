import heapq
from collections import deque

n = int(input())
time = deque()
for _ in range(n):
    p, q = map(int, input().split())
    time.append((p, q))
time = sorted(time)

computers = []
for i in range(n):
    heapq.heappush(computers, i)
end_time = []
mx_computer = 0
answer = [0] * n
for start, end in time:
    while end_time:
        if end_time[0][0] <= start:
            e, c = heapq.heappop(end_time)
            heapq.heappush(computers, c)
        else:
            break
    computer = heapq.heappop(computers)
    mx_computer = max(mx_computer, computer)
    answer[computer] += 1
    heapq.heappush(end_time, [end, computer])
print(mx_computer+1)
print(*answer[:mx_computer+1])