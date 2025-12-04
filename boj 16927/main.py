import sys

input = sys.stdin.readline

n, m, r = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
# 하, 우, 상, 좌
row = [1, 0, -1, 0]
col = [0, 1, 0, -1]

left = 0
right = m - 1
up = 0
down = n - 1
while left < right and up < down:
    for _ in range(r % ((right - left) * 2 + (down - up) * 2)):
        now = [left, up]
        now_tmp = arr[left][up]
        dir = 0
        while True:
            now[0] += row[dir]
            now[1] += col[dir]
            # now_tmp 이전값 now 앞으로 바꿀 인덱스
            now_tmp, arr[now[0]][now[1]] = arr[now[0]][now[1]], now_tmp
            if (dir == 0 and now[0] == down) or (dir == 1 and now[1] == right) or (dir == 2 and now[0] == up) or (
                    dir == 3 and now[1] == left):
                dir = (dir + 1) % 4
            if now[0] == left and now[1] == up:
                break
    left += 1
    right -= 1
    up += 1
    down -= 1
for i in range(n): print(' '.join(map(str, arr[i])))