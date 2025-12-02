n, m = map(int, input().split())
board = [[0 for _ in range(m)] for _ in range(n)]

block = list(map(int, input().split()))
for i, b in enumerate(block):
    for k in range(b):
        board[k][i] = 1

count = 0
# 0 벽을 안 만났을 때 | 1 벽을 만났을 때 | 2 벽을 만나고 밖으로 나왔을 때 | 3 벽을 만나고 다시 벽을 만났을 때
for i in range(n):
    flag = 0
    tmp = 0
    for j in range(m):
        # 벽을 만나면 flag를 1로
        if flag == 0 and board[i][j] == 1:
            flag = 1
        # 벽에서 나와서 빈공간으로 갈 때 flag를 2로
        elif flag == 1 and board[i][j] == 0:
            flag = 2
            tmp += 1

        # 벽을 만난상태에서 다시 벽을 만났을때
        elif flag == 2 and board[i][j] == 1:
            flag = 1
            count += tmp
            tmp = 0
        elif flag == 2 and board[i][j] == 0:
            tmp += 1



print(count)
