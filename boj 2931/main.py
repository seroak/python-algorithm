from collections import deque
import sys

input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def direction(s):
    if s == '|':
        return [1, 3]
    elif s == '-':
        return [0, 2]
    elif s == '+' or s == 'M' or s == 'Z':
        return [0, 1, 2, 3]
    elif s == '1':
        return [0, 1]
    elif s == '2':
        return [0, 3]
    elif s == '3':
        return [2, 3]
    elif s == '4':
        return [1, 2]


def bfs(x, y, dir):
    global fx, fy
    q = deque()
    q.append([x, y, dir])
    c[x][y] = 1
    while q:
        x, y, dir = q.popleft()
        for d in dir:
            nx = x + dx[d]
            ny = y + dy[d]
            # 범위안에 있고 아직 방문을 하지 않았을때
            if 0 <= nx < m and 0 <= ny < n and not c[nx][ny]:
                # 가스관을 타고 왔는데 다음 위치가 빈곳이 아닐 때
                if a[nx][ny] != ".":
                    c[nx][ny] = 1
                    # 해당하는 가스관이 갈 수 있는 곳
                    ndir = direction(a[nx][ny])
                    q.append([nx, ny, ndir])
                # 가스관을 타고 왔는데 다음 위치가 빈곳인 경우
                else:
                    # 현재 위치가 M 또는 Z는 괜찮으니 continue
                    if a[x][y] == "M" or a[x][y] == "Z":
                        continue
                    # 출력용 좌표를 위해서 +1을 한다

                    fx, fy = nx + 1, ny + 1
                    # 들어온 가스의 방향을 거꾸로해서 빈 부분이 어느 방향으로 가는 가스관을 연결해야하는지 확인
                    nd = (d + 2) % 4
                    # nd가 중복이 아니면 넣는다
                    if nd not in check_list:
                        check_list.append(nd)


m, n = map(int, input().split())
c = [[0] * n for _ in range(m)]

a = []
for i in range(m):
    row = list(input().strip())
    a.append(row)
    for j in range(n):
        # 출발지하고 도착지 확인
        if row[j] == "M":
            sx, sy = i, j
        elif row[j] == "Z":
            zx, zy = i, j
check_list, fx, fy = [], 0, 0
bfs(sx, sy, [0, 1, 2, 3])
bfs(zx, zy, [0, 1, 2, 3])

# + 가 사라져서 섬처럼 남은 부분이 있을 수 있으니까 그 부분도 bfs로 찾아준다
for i in range(m):
    for j in range(n):
        # 빈공간도 아니고 방문도 하지 않은곳
        if a[i][j] != "." and not c[i][j]:
            bfs(i, j, direction(a[i][j]))
check_list.sort()
if len(check_list) == 4:
    print(fx, fy, '+')
else:
    for i in ["-", "|", "1", "2", "3", "4"]:
        if check_list == direction(i):
            print(fx, fy, i)
