import sys
input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
route = list()
visited = [[False] * n for _ in range(n)]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
for _ in range(m):
    a, b = map(int, input().split())
    route.append([a,b])
    board[a-1][b-1] = 2
