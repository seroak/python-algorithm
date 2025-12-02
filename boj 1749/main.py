n, m = map(int, input().split())
board = []
for _ in range(n):
    arr = list(map(int, input().split()))
    board.append(arr)
for i in range(n):
    for j in range(m):
        if 0 <= i - 1:
            board[i][j] += board[i-1][j]
        if 0 <= j - 1:
            board[i][j] += board[i][j-1]
        if 0 <= i - 1 and 0 <= j - 1:
            board[i][j] -= board[i-1][j-1]
answer = -float('inf')
for i in range(n):
    for j in range(m):
        answer = max(answer, board[i][j])
        for cur_i in range(i+1):
            for cur_j in range(j+1):
                num = board[i][j]
                if cur_i > 0:
                    num -= board[cur_i-1][j]
                if cur_j > 0:
                    num -= board[i][cur_j-1]
                if cur_i > 0 and cur_j > 0:
                    num += board[cur_i-1][cur_j-1]
                answer = max(answer, num)
print(answer)