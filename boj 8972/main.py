from collections import defaultdict


def sol():
    r, c = map(int, input().split())
    board = [list(map(str, input().rstrip())) for _ in range(r)]
    dist = list(map(int, input().rstrip()))
    dx_dy = [[], [1, -1], [1, 0], [1, 1], [0, -1], [0, 0], [0, 1], [-1, -1], [-1, 0], [-1, 1]]
    arduino_dx_dy = [[1, -1], [1, 0], [1, 1], [0, -1], [0, 1], [-1, -1], [-1, 0], [-1, 1]]
    crazy_arduino = list()
    for i in range(r):
        for j in range(c):
            if board[i][j] == "R":
                crazy_arduino.append([i, j])
            if board[i][j] == "I":
                jong_su = [i, j]
    count = 0
    for i in dist:
        count += 1
        dx, dy = dx_dy[i]
        x, y = jong_su
        nx = x + dx
        ny = y + dy
        if board[nx][ny] == "R":

            print("kraj", count)
            return
        jong_su = [nx, ny]
        board[x][y] = "."  # 원래 종수가 있던 곳 .으로
        board[nx][ny] = "I"  # 종수가 새로 움직인 곳
        arduino_xy = defaultdict(list)  # 폭팔한 곳을 찾기 위해 먼저 아두이누가 움직인 곳을 dict에 저장
        for ax, ay in crazy_arduino:
            max_dist = [200, -1, -1]
            for k in range(8):
                nax = ax + arduino_dx_dy[k][0]
                nay = ay + arduino_dx_dy[k][1]
                d = abs(nx - nax) + abs(ny - nay)
                if max_dist[0] > d:
                    max_dist = [d, nax, nay]
            board[ax][ay] = "."
            if max_dist[1] == nx and max_dist[2] == ny:

                print("kraj", count)
                return
            arduino_xy[tuple([max_dist[1], max_dist[2]])].append([max_dist[1], max_dist[2]])  # 아두이누가 움직인 곳을 dict에 저장
        tmp = list()
        for item in arduino_xy:
            # 아두이누가 둘 이상 모여있으면 폭팔하므로 전부 지운다
            if len(arduino_xy[item]) > 1:
                continue
            ard_x, ard_y = arduino_xy[item][0]
            board[ard_x][ard_y] = "R"
            tmp.append([ard_x, ard_y])
        crazy_arduino = tmp
    for i in board:
        print(''.join(i))



sol()
