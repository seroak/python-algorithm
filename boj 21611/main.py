n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

blizzard_dx = [-1, 1, 0, 0]
blizzard_dy = [0, 0, -1, 1]

ans = 0


def rotate():
    route = []
    r = n // 2
    c = n // 2
    scope = 1  # 지금 한 방향으로 움직일 수 있는 거리
    dist = 0  # 가는 방향
    change_scope = 0
    while True:
        if change_scope == 2:
            change_scope = 0
            scope += 1
        for _ in range(scope):
            r += dx[dist]
            c += dy[dist]
            route.append([r, c])
            if r == 0 and c == 0:
                return route
        change_scope += 1
        dist += 1
        dist %= 4


def arrange(search_route):
    while True:
        flag = False
        for i in range(len(search_route) - 1):
            x1 = search_route[i][0]
            y1 = search_route[i][1]
            x2 = search_route[i + 1][0]
            y2 = search_route[i + 1][1]
            if board[x1][y1] == 0 and board[x2][y2] != 0:
                board[x1][y1] = board[x2][y2]
                board[x2][y2] = 0
                flag = True
        if flag is False:
            break


def destroy_and_arrange(search_route, s, d):
    r = n // 2
    c = n // 2
    for _ in range(s):
        r += blizzard_dx[d - 1]
        c += blizzard_dy[d - 1]
        board[r][c] = 0
    arrange(search_route)


def explore(search_route):
    global ans
    while True:
        prev = board[search_route[0][0]][search_route[0][1]]
        explore_blocks = []
        sames = []
        for x, y in search_route:
            if prev == board[x][y]:
                sames.append([x, y])
            else:
                if len(sames) >= 4:
                    explore_blocks.append(sames)
                prev = board[x][y]
                sames = [[x, y]]

        if len(explore_blocks) == 0:
            return
        else:
            for explore_block in explore_blocks:
                idx_x = explore_block[0][0]
                idx_y = explore_block[0][1]
                if board[idx_x][idx_y] == 1:
                    ans += len(explore_block)
                if board[idx_x][idx_y] == 2:
                    ans += 2 * len(explore_block)
                if board[idx_x][idx_y] == 3:
                    ans += 3 * len(explore_block)
                for x, y in explore_block:
                    board[x][y] = 0
            arrange(search_route)


def change_block(search_route):
    change_board = [[0] * n for _ in range(n)]
    prev_block = board[search_route[0][0]][search_route[0][1]]
    count = 0
    change_list = []  # 수가 변해야하는 [숫자 블록 수, 숫자]
    for x, y in search_route:
        if prev_block == board[x][y]:
            count += 1
        else:
            change_list.append(count)
            change_list.append(prev_block)
            count = 1
            prev_block = board[x][y]

    for i in range(len(search_route)):
        if len(change_list) <= i:
            break
        x = search_route[i][0]
        y = search_route[i][1]
        change_board[x][y] = change_list[i]
    return change_board


search_route = rotate()

for _ in range(m):
    d, s = map(int, input().split())
    destroy_and_arrange(search_route, s, d)
    explore(search_route)
    board = change_block(search_route)

print(ans)