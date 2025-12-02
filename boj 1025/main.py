import sys
input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]


def check(num):
    s = int(num)
    return int(s ** 0.5) ** 2 == s


mx = -1
for i in range(n):
    for j in range(m):
        for row_d in range(-n, n):
            for col_d in range(-m, m):
                if row_d == 0 and col_d == 0:
                    continue
                x = i
                y = j
                num = ""
                while 0 <= x < n and 0 <= y < m:
                    num += board[x][y]

                    if check(int(num)):
                        mx = max(mx, int(num))
                    x += row_d
                    y += col_d
if mx == -1:
    print(-1)
else:
    print(mx)
