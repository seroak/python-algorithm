import sys
input = sys.stdin.readline
n = int(input())
like = [[] for _ in range(n * n + 1)]
board = [[0 for _ in range(n)] for _ in range(n)]
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
for _ in range(n * n):
    tmp = list(map(int, input().split()))

    for i in tmp[1:]:
        like[tmp[0]].append(i)
    # 1. 비어있는 칸 중에서 좋아하는 학생이 가장 많이 인접한 칸으로 자리를 정한
    like_board = [[-1 for _ in range(n)] for _ in range(n)]
    mx_like_point = 0  # 최대 호감도가 무었인지 체크
    for i in range(n):
        for j in range(n):
            # 칸이 비어있으면
            if board[i][j] == 0:
                like_point = 0
                # 네 방향 탐색
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        # board가 비어있지 않으면
                        if board[nx][ny] != 0:
                            # 좋아하는 학생인지 체크
                            for q in tmp[1:]:
                                if q == board[nx][ny]:
                                    like_point += 1
                like_board[i][j] = like_point
                mx_like_point = max(like_point, mx_like_point)
    rule_1 = list()
    for i in range(n):
        for j in range(n):
            if like_board[i][j] == mx_like_point:
                rule_1.append([i, j])

    # 1번 조건으로 나온것이 한개라면 해당 자리에 학생을 위치키고 continue
    if len(rule_1) == 1:
        x, y = rule_1.pop()
        board[x][y] = tmp[0]
        continue

    # 2. 1을 만족하는 칸이 여러 개이면, 1번 조건을 만족하는 칸의 인접한 칸들이 가장 많이 비어있는 칸을 자리로 정한다.
    empty_board = [[-1 for _ in range(n)] for _ in range(n)]
    mx_empty_point = 0
    if len(rule_1) >= 2:
        for x, y in rule_1:
            empty_point = 0
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    if board[nx][ny] == 0:
                        empty_point += 1
            empty_board[x][y] = empty_point
            mx_empty_point = max(empty_point, mx_empty_point)
    rule_2 = list()
    for i in range(n):
        for j in range(n):
            if empty_board[i][j] == mx_empty_point:
                rule_2.append([i, j])

    # 2번 조건으로 나온 값이 한개라면 해당 자리에 학생을 위치키고 continue
    if len(rule_2) == 1:
        x, y = rule_2.pop()
        board[x][y] = tmp[0]
        continue

    # 3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
    if len(rule_2) >= 2:
        rule_2.sort(key=lambda w: (w[0], w[1]))

        x, y = rule_2[0]
        board[x][y] = tmp[0]

answer = 0
for i in range(n):
    for j in range(n):
        count = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] in like[board[i][j]]:
                    count += 1
        if count == 0:
            answer += 0
        elif count == 1:
            answer += 1
        elif count == 2:
            answer += 10
        elif count == 3:
            answer += 100
        else:
            answer += 1000

print(answer)
