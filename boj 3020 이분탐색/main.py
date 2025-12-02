import sys
import bisect

# 입력 받기
n, h = map(int, sys.stdin.readline().split())

down = []
up = []

for _ in range(n // 2):
    down.append(int(sys.stdin.readline()))
    up.append(int(sys.stdin.readline()))

# 정렬 (이진탐색을 위해)
down.sort()
up.sort()
print(down)
print(up)
# 최소 장애물 개수 및 해당 층 개수 찾기
min_obstacles = n
count = 0

for i in range(1, h + 1):
    # 현재 높이 `i`에서 부딪히는 장애물 개수
    down_count = len(down) - bisect.bisect_left(down, i)
    up_count = len(up) - bisect.bisect_left(up, h - i + 1)
    total_obstacles = down_count + up_count

    if total_obstacles == min_obstacles:
        count += 1
    elif total_obstacles < min_obstacles:
        min_obstacles = total_obstacles
        count = 1

# 결과 출력
print(min_obstacles, count)