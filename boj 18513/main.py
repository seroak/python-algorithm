from collections import deque

# 입력 처리
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
water = list(map(int, input().split()))

vis_set = set()
queue = deque()

for w in water:
    queue.append((w, 0))
    vis_set.add(w)

answer = 0
count = 0

while count < k + n:
    index, dist = queue.popleft()
    answer += dist

    if (index - 1) not in vis_set:
        vis_set.add(index - 1)
        queue.append((index - 1, dist + 1))

    if (index + 1) not in vis_set:
        vis_set.add(index + 1)
        queue.append((index + 1, dist + 1))

    count += 1

print(answer)