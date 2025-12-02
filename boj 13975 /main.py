import heapq

t = int(input())
for _ in range(t):
    k = int(input())
    heap = list(map(int, input().split()))
    heapq.heapify(heap)
    ans = 0
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        c = a + b
        heapq.heappush(heap, c)
        ans += c
    print(ans)
