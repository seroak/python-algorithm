import heapq

n, k = map(int, input().split())
customers = []
for _ in range(n):
    id, w = map(int, input().split())
    customers.append([id, w])
heap = []
for i in range(k):
    heapq.heappush(heap, [0, i + 1])
customers_info = []
for id, w in customers:
    time, i = heapq.heappop(heap)
    customers_info.append((time + w, i, id))
    heapq.heappush(heap, [time + w, i])

customers_info.sort(key=lambda x: (x[0], -x[1]))

answer = 0
for i, item in enumerate(customers_info):
    answer += (i+1) * item[2]

print(answer)