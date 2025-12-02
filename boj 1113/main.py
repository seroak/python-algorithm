from collections import deque
import copy
import sys

n, m = map(int, input().split())
board = list()
for i in range(n):
    tmp = list(map(int, input().rstrip()))
    board.append(tmp)

# 물이 고일 수 있는 장소
water = [[False for _ in range(m)] for _ in range(n)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
check_visited = [[False for _ in range(m)] for _ in range(n)]


def bfs(x, y):
    global water
    queue = deque()
    queue.append([x, y])
    tmp_water = copy.deepcopy(water)
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[x][y] = True
    tmp_water[x][y] = True
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            # 이전 위치보다 현재 위치가 같거나 낮으면 물이 흐를 수 있으므로 진행 하고 이번 탐색에서 방문한적이 없어야한다
            if board[nx][ny] <= board[x][y] and visited[nx][ny] is False:
                if 1 <= nx < n - 1 and 1 <= ny < m - 1:
                    tmp_water[nx][ny] = True
                    visited[nx][ny] = True
                    queue.append([nx, ny])
                else:
                    # 밖으로 나가는 경우 카피를 하지 않고 넘어감
                    return

    water = copy.deepcopy(tmp_water)
    return


def bfs_check(x, y):
    queue = deque()
    queue.append([x, y])
    check_visited[x][y] = True
    mn = sys.maxsize
    cnt = 1
    height = board[x][y]
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            # 물이 있는 곳이고 아직 못가 본가본 곳이면 탐색
            if water[nx][ny] and check_visited[nx][ny] is False:
                queue.append([nx, ny])
                check_visited[nx][ny] = True
                cnt += 1
                height += board[nx][ny]
            elif water[nx][ny] is False:
                check_visited[nx][ny] = True
                mn = min(mn, board[nx][ny])
    w = (mn * cnt) - height
    return w


for i in range(1, n - 1):
    for j in range(1, m - 1):
        if water[i][j] is False:
            bfs(i, j)

answer = 0
for i in range(1, n - 1):
    for j in range(1, m - 1):
        if water[i][j] is True and check_visited[i][j] is False:
            answer += bfs_check(i, j)
print(answer)
