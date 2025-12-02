import heapq
import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    answer = 1
    n = int(input())
    slime = list(map(int, input().split()))
    heapq.heapify(slime)

    while len(slime) > 1:
        a = heapq.heappop(slime)
        b = heapq.heappop(slime)
        cal = (a * b)
        answer = (answer * (cal % 1000000007)) % 1000000007
        heapq.heappush(slime, cal)

    print(answer)