import sys
from collections import deque
input = sys.stdin.readline
n, m, g, r = map(int, input().split())
board = []
for i in range(n):
    tmp = list(map(int, input().split()))
    board.append(tmp)

avail_land = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            avail_land.append([i, j])
comb = []

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def comb_red(avail_land, g, r, visited, cur, green_arr, red_arr, depth):
    if depth == r:
        comb.append([green_arr[:], red_arr[:]])
        return
    for i in range(cur, len(avail_land)):
        if visited[i] is False:
            visited[i] = True
            red_arr.append(avail_land[i])
            comb_red(avail_land, g, r, visited, i + 1, green_arr, red_arr, depth + 1)
            red_arr.pop()
            visited[i] = False


def comb_green(avail_land, g, r, visited, cur, green_arr, red_arr, depth):
    if depth == g:
        comb_red(avail_land, g, r, visited, 0, green_arr, red_arr, 0)
        return
    for i in range(cur, len(avail_land)):
        if visited[i] is False:
            visited[i] = True
            green_arr.append(avail_land[i])
            comb_green(avail_land, g, r, visited, i + 1, green_arr, red_arr, depth + 1)
            green_arr.pop()
            visited[i] = False


def combination(avail_land, g, r):
    visited = [False] * len(avail_land)
    comb_green(avail_land, g, r, visited, 0, [], [], 0)
    answer = 0
    for red, green in comb:
        # 빨간색 배양액 1 초록색 배양액 2 new 빨간색 배양액 3 new 초록색 배양앵 4 꽃이 핀 곳 5
        check_board = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if board[i][j] == 0:
                    check_board[i][j] = 6
        count = 0

        red_queue = deque()
        green_queue = deque()
        for r in red:
            red_queue.append(r)
            check_board[r[0]][r[1]] = 1
        for g in green:
            green_queue.append(g)
            check_board[g[0]][g[1]] = 2
        while not (len(red_queue) == 0 and len(green_queue) == 0):
            len_red = len(red_queue)
            new_arr = []
            for _ in range(len_red):
                x, y = red_queue.popleft()
                if check_board[x][y] != 1:
                    continue
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < m:
                        # board가 0 이여서 배양액이 퍼질 수 있어야하고
                        # check_board가 -1 이여서 배양액이 퍼진적 없는 곳이여야한다
                        # red는 green이 퍼진적이 없으니까 꽃 체크는 하지 않아도 된다
                        if board[nx][ny] != 0 and check_board[nx][ny] == 0:
                            # 배양액이 퍼진곳을 체크
                            check_board[nx][ny] = 3
                            new_arr.append([nx, ny])
                            red_queue.append([nx, ny])

            len_green = len(green_queue)
            for _ in range(len_green):
                x, y = green_queue.popleft()
                if check_board[x][y] != 2:
                    continue
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < m:
                        if board[nx][ny] != 0 and check_board[nx][ny] == 0:
                            # 배양액이 퍼진곳을 체크
                            check_board[nx][ny] = 4
                            new_arr.append([nx, ny])
                            green_queue.append([nx, ny])
                        elif board[nx][ny] != 0 and check_board[nx][ny] == 3:
                            check_board[nx][ny] = 5
                            count += 1

            for x, y in new_arr:
                if check_board[x][y] == 3:
                    check_board[x][y] = 1
                if check_board[x][y] == 4:
                    check_board[x][y] = 2
        answer = max(count, answer)


    print(answer)

combination(avail_land, g, r)
