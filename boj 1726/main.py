import sys
from collections import deque

input = sys.stdin.readline
# 동 서 남 북
dr = (0, 0, 1, -1)
dc = (1, -1, 0, 0)
change_dir = ((2, 3), (2, 3), (0, 1), (0, 1))
R, C = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]

sr, sc, sd = map(int, input().split())
gr, gc, gd = map(int, input().split())


def bfs():
    visited = [[[0] * 4 for _ in range(C)] for _ in range(R)]
    Q = deque()
    Q.append([sr - 1, sc - 1, sd - 1, 0])
    visited[sr - 1][sc - 1][sd - 1] = 1
    while Q:
        r, c, d, cnt = Q.popleft()
        # print(x, y, direction)
        if (r, c, d) == (gr - 1, gc - 1, gd - 1):  # (목표위치와 방향)에 도착하면 cnt 리턴
            return cnt
        # 1,2,3 직진
        for dis in range(1, 4):
            nr = r + dr[d] * dis
            nc = c + dc[d] * dis
            nd = d
            if not (0 <= nr < R and 0 <= nc < C) or A[nr][nc] == 1:
                break
            if visited[nr][nc][nd] == 0:
                Q.append([nr, nc, nd, cnt + 1])
                visited[nr][nc][nd] = 1
        for nd in change_dir[d]:
            if visited[r][c][nd] == 0:
                visited[r][c][nd] = 1
                Q.append([r, c, nd, cnt + 1])


print(bfs())
