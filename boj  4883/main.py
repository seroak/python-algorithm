import sys
inf = sys.maxsize
count = 1
dx = [0, 1, 1, 1]
dy = [1, -1, 0, 1]
while True:
    n = int(input())
    if n == 0:
        break
    board = list()
    dp = list()
    for _ in range(n):
        tmp = list(map(int, input().split()))
        board.append(tmp)

    dp = [[inf for _ in range(3)] for _ in range(n)]
    dp[0][1] = board[0][1]
    for i in range(n):
        for j in range(3):
            if i == 0 and j == 0:
                continue
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < n and 0 <= ny < 3:
                    dp[nx][ny] = min(dp[nx][ny], dp[i][j] + board[nx][ny])

  
    print(f"{count}. {dp[-1][1]}")
    count += 1
