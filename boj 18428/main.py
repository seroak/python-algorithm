n = int(input())
board = [list(map(str, input().split())) for _ in range(n)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

student = list()
for i in range(n):
    for j in range(n):
        if "S" == board[i][j]:
            student.append([i, j])

check_board = list()
for x, y in student:

    for i in range(4):
        nx = x
        ny = y
        tmp = list()
        while True:
            nx = dx[i] + nx
            ny = dy[i] + ny
            tmp.append([nx, ny])
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                break
            if board[nx][ny] == "T":
                for sublist in tmp[:-1]:
                    if sublist not in check_board:
                        check_board.append(sublist)
                break


check_board.extend(student)
def sol():
    if len(check_board) == 0:
        print("YES")
        return
    for i in range(len(check_board) - 2):
        for j in range(i+1, len(check_board) - 1):
            for k in range(j+1, len(check_board)):
                answer = True

                x1, y1 = check_board[i]
                x2, y2 = check_board[j]
                x3, y3 = check_board[k]
                board[x1][y1] = "O"
                board[x2][y2] = "O"
                board[x3][y3] = "O"
                for x, y in student:
                    for q in range(4):
                        nx = x
                        ny = y
                        flag = False
                        while True:
                            nx = dx[q] + nx
                            ny = dy[q] + ny
                            if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] == "O":
                                break
                            if board[nx][ny] == "T":
                                flag = True
                        if flag is True:
                            answer = False
                if answer is True:
                    print("YES")
                    return
                board[x1][y1] = "X"
                board[x2][y2] = "X"
                board[x3][y3] = "X"
    print("NO")
sol()