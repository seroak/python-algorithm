import sys

# 입력 받기
n, h = map(int, sys.stdin.readline().split())

down_count = [0] * (h + 2)
up_count = [0] * (h + 2)

# 장애물 높이 개수 카운트
for _ in range(n // 2):
    down_count[int(sys.stdin.readline())] += 1
    up_count[h - int(sys.stdin.readline()) + 1] += 1

# 누적합 계산
for i in range(1, h + 1):
    down_count[i] += down_count[i - 1]

for i in range(h, 0, -1):
    up_count[i] += up_count[i + 1]

# 최소 장애물 개수 찾기
min_obstacles = n
count = 0

for i in range(1, h + 1):
    total_obstacles = (down_count[h] - down_count[i - 1]) + (up_count[1] - up_count[i + 1])

    if total_obstacles == min_obstacles:
        count += 1
    elif total_obstacles < min_obstacles:
        min_obstacles = total_obstacles
        count = 1

# 결과 출력
print(min_obstacles, count)