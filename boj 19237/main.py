n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
# 1: 위 2: 아래 3: 왼쪽 4: 오른쪽
dx_dy = ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1))
shark_dist = list(map(int, input().split()))
shark_priority = list()
for _ in range(m):
    tmp = list()
    for _ in range(4):
        priority = list(map(int, input().split()))
        tmp.append(priority)
    shark_priority.append(tmp)
for i in shark_priority:
    print(i)
