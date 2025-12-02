from collections import deque

n, m, t = map(int, input().split())
board = [deque(map(int, input().split())) for _ in range(n)]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
for i in range(t):
    x, d, k = map(int, input().split())
    tmp_x = x
    # x의 배수의 원판을 순회
    while tmp_x <= n:

        for _ in range(k):

            if d == 0:
                right = board[tmp_x - 1].pop()
                board[tmp_x - 1].appendleft(right)
            if d == 1:
                left = board[tmp_x - 1].popleft()
                board[tmp_x - 1].append(left)
        tmp_x += x
    # 원판을 돌린 후 인접한 숫자가 있는지 확인
    check = [[False] * m for _ in range(n)]
    flag = False

    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                continue
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                # 위, 아래로 나갔을 때
                if nx < 0 or nx >= n:
                    continue
                # 오른쪽 왼쪽으로 나가면 모듈러 연산을 한다
                ny %= m
                if board[nx][ny] == 0:
                    continue
                if board[nx][ny] == board[i][j]:
                    flag = True
                    check[i][j] = True
                    check[nx][ny] = True

    # 확인을해서 인접한 수가 있을 때 인접한 수는 0으로
    if flag is True:
        for i in range(n):
            for j in range(m):
                if check[i][j] is True:
                    board[i][j] = 0
    # 인접한 수가 없다면 평균을 구해서 크면 -1 작으면 +1
    else:
        total = 0
        cnt = 0
        for i in range(n):
            for j in range(m):
                if board[i][j] != 0:
                    total += board[i][j]
                    cnt += 1
        if cnt > 0:
            ave = total / cnt

            for i in range(n):
                for j in range(m):
                    if board[i][j] == 0:
                        continue
                    if float(board[i][j]) < ave:
                        board[i][j] += 1
                    elif float(board[i][j]) > ave:
                        board[i][j] -= 1

ans = 0
for i in range(n):
    for j in range(m):
        ans += board[i][j]
print(ans)
