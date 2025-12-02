import sys
input = sys.stdin.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
board_3D = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(3)]

board_3D[0][0][1] = 1

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            continue
        # k == 0 가로/ k == 1 세로/ k == 2 대각선
        for k in range(3):
            if board_3D[k][i][j] != 0:
                if k == 0:
                    if j + 1 < n and board[i][j + 1] == 0:
                        board_3D[0][i][j + 1] += board_3D[0][i][j]
                    if j + 1 < n and i + 1 < n and board[i + 1][j + 1] == 0 and board[i + 1][j] == 0 and board[i][
                        j + 1] == 0:
                        board_3D[2][i + 1][j + 1] += board_3D[0][i][j]
                if k == 1:
                    if i + 1 < n and board[i + 1][j] == 0:
                        board_3D[1][i + 1][j] += board_3D[1][i][j]
                    if i + 1 < n and j + 1 < n and board[i + 1][j + 1] == 0 and board[i + 1][j] == 0 and board[i][
                        j + 1] == 0:
                        board_3D[2][i + 1][j + 1] += board_3D[1][i][j]
                if k == 2:
                    if j + 1 < n and board[i][j + 1] == 0:
                        board_3D[0][i][j + 1] += board_3D[2][i][j]
                    if i + 1 < n and board[i + 1][j] == 0:
                        board_3D[1][i + 1][j] += board_3D[2][i][j]
                    if i + 1 < n and j + 1 < n and board[i + 1][j + 1] == 0 and board[i + 1][j] == 0 and board[i][
                        j + 1] == 0:
                        board_3D[2][i + 1][j + 1] += board_3D[2][i][j]


print(board_3D[0][-1][-1] + board_3D[1][-1][-1] + board_3D[2][-1][-1])
