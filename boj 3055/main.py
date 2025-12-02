r, c = map(int, input().split())
board = list()
for i in range(r):
    tmp = list(map(str, input().rstrip()))
    board.append(tmp)

water = list()
hog = list()
hall = list()
visited_water = [[False for _ in range(c)] for _ in range(r)]
visited_hog = [[False for _ in range(c)] for _ in range(r)]
for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j] == "*":
            water.append([i, j])
            visited_water[i][j] = True
        if board[i][j] == "S":
            hog.append([i, j])
        if board[i][j] == "D":
            hall = [i, j]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
count = 1
while hog:
    tmp_water = list()
    while water:
        x, y = water.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if visited_water[nx][ny] is True:
                    continue
                if board[nx][ny] == "X":
                    continue
                if board[nx][ny] == "D":
                    continue
                tmp_water.append([nx, ny])
                visited_water[nx][ny] = True
    water = tmp_water
    tmp_hog = list()
    while hog:
        x, y = hog.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if visited_hog[nx][ny] is True:
                    continue
                if board[nx][ny] == "X":
                    continue
                if visited_water[nx][ny] is False:
                    tmp_hog.append([nx, ny])
                    visited_hog[nx][ny] = True
                if nx == hall[0] and ny == hall[1]:
                    print(count)
                    exit(0)
    hog = tmp_hog
    count += 1
print("KAKTUS")