import heapq

t = int(input())
for _ in range(t):
    heap = list()
    n = int(input())
    arr = list()
    for _ in range((n // 10) + 1):
        tmp = list(map(int, input().split()))
        arr.extend(tmp)

    answer = list()
    for i in arr:
        heapq.heappush(heap, i)
        tmp = list()
        if len(heap) % 2 == 1:
            for k in range((len(heap) // 2) + 1):
                num = heapq.heappop(heap)
                tmp.append(num)
            answer.append(tmp[-1])
            for q in tmp:
                heapq.heappush(heap, q)
    print(len(answer))
    count = 0
    for i in answer:
        print(i, end=" ")
        count += 1
        if count == 10:
            print()
            count = 0
