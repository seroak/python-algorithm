import heapq
n = int(input())
lecture = []
for _ in range(n):
    num, start, end = map(int, input().split())
    lecture.append([start, end])
lecture.sort()

start, end = lecture[0]
heap = list()
count = 0
for start, end in lecture:
    if len(heap) == 0:
        heapq.heappush(heap, end)
        count += 1
        continue
    if heap[0] <= start:
        heapq.heappop(heap)
    else:
        count += 1
    heapq.heappush(heap, end)
print(count)