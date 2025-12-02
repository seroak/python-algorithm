import math
import sys
input = sys.stdin.readline
n = int(input())
board = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    board.append(tmp)
# dist 0 왼쪽은 그대로 사용 | dist 1 = 아레 x y 순서 바꾸고 -로 전환 | dist 2 오른쪽은 -로 전환 | dist 3 위는 x y 순서 바꾸기
spread = [[0, -2, 0.05], [-1, -1, 0.1], [1, -1, 0.1], [1, 0, 0.07], [-1, 0, 0.07], [-2, 0, 0.02], [2, 0, 0.02],
          [1, 1, 0.01], [-1, 1, 0.01]]
answer = 0


def sand(r, c, dist):
    global answer
    if dist == 0:
        acc = 0
        for x, y, per in spread:
            tmp = math.floor(board[r][c] * per)
            nr = r + x
            nc = c + y
            if 0 <= nr < n and 0 <= nc < n:
                board[nr][nc] += tmp
            else:  # 범위를 벗어나면 answer에 더해줌
                answer += tmp
            acc += tmp
        nr = r
        nc = c - 1
        if 0 <= nr < n and 0 <= nc < n:
            board[nr][nc] += board[r][c] - acc
        else:
            answer += board[r][c] - acc
    elif dist == 1:
        acc = 0
        for x, y, per in spread:
            tmp = math.floor(board[r][c] * per)
            nr = r - y
            nc = c - x
            if 0 <= nr < n and 0 <= nc < n:
                board[nr][nc] += tmp
            else:
                answer += tmp
            acc += tmp
        nr = r + 1
        nc = c
        if 0 <= nr < n and 0 <= nc < n:
            board[nr][nc] += board[r][c] - acc
        else:
            answer += board[r][c] - acc
    elif dist == 2:  # dist 2 오른쪽은 -로 전환
        acc = 0
        for x, y, per in spread:
            tmp = math.floor(board[r][c] * per)
            nr = r - x
            nc = c - y
            if 0 <= nr < n and 0 <= nc < n:
                board[nr][nc] += tmp
            else:  # 범위를 벗어나면 answer에 더해줌
                answer += tmp
            acc += tmp
        nr = r
        nc = c + 1
        if 0 <= nr < n and 0 <= nc < n:
            board[nr][nc] += board[r][c] - acc
        else:
            answer += board[r][c] - acc
    else:
        acc = 0
        for x, y, per in spread:  # dist 3 위는 x y 순서 바꾸기
            tmp = math.floor(board[r][c] * per)
            nr = r + y
            nc = c + x
            if 0 <= nr < n and 0 <= nc < n:
                board[nr][nc] += tmp
            else:  # 범위를 벗어나면 answer에 더해줌
                answer += tmp
            acc += tmp
        nr = r - 1
        nc = c
        if 0 <= nr < n and 0 <= nc < n:
            board[nr][nc] += board[r][c] - acc
        else:
            answer += board[r][c] - acc



def solution(n):
    r, c = n // 2, n // 2
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    step = 1  # 토네이도가 가야하는 최대 거리
    dist = 0  # 토네이도의 방향
    cycle = 0  # 사이클이 2번 돌면 토네이도의 최대 거리 증가
    while True:
        # 토네이도의 최대거리 만큼 증가
        for i in range(step):

            r = r + dx[dist]
            c = c + dy[dist]
            sand(r, c, dist)
            if r == 0 and c == 0:
                return
        cycle += 1
        dist = (dist + 1) % 4
        # 사이클이 두번 돌면  토네이도의 최대 거리 증가
        if cycle == 2:
            cycle = 0
            step += 1


solution(n)

print(answer)
