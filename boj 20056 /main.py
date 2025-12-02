import copy
import sys

n, m, k = map(int, input().split())
fireballs = []
for i in range(m):
    tmp = list(map(int, input().split()))
    tmp[0] -= 1
    tmp[1] -= 1
    fireballs.append(tmp)
dir = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

board = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(k):

    while fireballs:
        r, c, m, s, d = fireballs.pop(0)
        nx = s * dir[d][0]
        ny = s * dir[d][1]
        nr = (r + nx) % n
        nc = (c + ny) % n
        board[nr][nc].append([m, s, d])


    for i in range(n):
        for j in range(n):
            if len(board[i][j]) > 1:
                sum_m, sum_s, cnt_odd, cnt_even, cnt = 0, 0, 0, 0, len(board[i][j])
                while board[i][j]:
                    _m, _s, _d = board[i][j].pop(0)
                    sum_m += _m
                    sum_s += _s
                    if _d % 2:
                        cnt_odd += 1
                    else:
                        cnt_even += 1
                if cnt_odd == cnt or cnt_even == cnt:
                    nd = [0, 2, 4, 6]
                else:
                    nd = [1, 3, 5, 7]
                if sum_m // 5:  # 질량 0이면 소멸
                    for d in nd:
                        fireballs.append([i,j, sum_m // 5, sum_s // cnt, d])
            # 1개인 경우
            if len(board[i][j]) == 1:
                fireballs.append([i, j] + board[i][j].pop())

answer = 0

for i in fireballs:
    answer += i[2]
print(answer)