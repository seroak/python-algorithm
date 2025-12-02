import heapq

n = int(input())
min_heap = []
max_heap = []
problem = dict()
for _ in range(n):
    p, l = map(int, input().split())
    heapq.heappush(min_heap, (l, p))
    heapq.heappush(max_heap, (-l, -p))
    problem[p] = l

m = int(input())
for _ in range(m):
    order = list(map(str, input().split()))
    if order[0] == "recommend":

        if int(order[1]) == 1:
            while True:
                # 문제 난이도
                l = -max_heap[0][0]
                # 문제 번호
                p = -max_heap[0][1]
                # 문제가 사라진 경우
                if not problem.get(p):
                    heapq.heappop(max_heap)
                    continue

                # 문제의 난이도가 달라진 경우
                if problem[p] != l:
                    heapq.heappop(max_heap)
                    continue

                print(-max_heap[0][1])
                break
        elif int(order[1]) == -1:
            while True:
                # 문제 난이도
                l = min_heap[0][0]
                # 문제 번호
                p = min_heap[0][1]
                # 문제가 사라진 경우
                if not problem.get(p):
                    heapq.heappop(min_heap)
                    continue

                # 문제의 난이도가 달라진 경우
                if problem[p] != l:
                    heapq.heappop(min_heap)
                    continue

                print(min_heap[0][1])
                break
    elif order[0] == "add":
        p = int(order[1]) # 문제 번호
        l = int(order[2]) # 문제 난이도
        problem[p] = l
        heapq.heappush(max_heap, (-l, -p))
        heapq.heappush(min_heap, (l, p))

    elif order[0] == "solved":
        p = int(order[1])
        del problem[p]

