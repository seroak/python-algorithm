import sys
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())
board = []
prefix = [[[0, 0] for _ in range(m)] for _ in range(n)]

for i in range(n):
    tmp = list(map(int, input().split()))
    board.append(tmp)
for i in range(n):
    for j in range(m):
        # row
        prefix[i][j][0] = (0 if i == 0 else prefix[i - 1][j][0]) + board[i][j]
        # col
        prefix[i][j][1] = (0 if j == 0 else prefix[i][j - 1][1]) + board[i][j]

row = [(prefix[i][m - 1][1], i) for i in range(n)]
col = [(prefix[n - 1][i][0], i) for i in range(m)]

heapq.heapify(row)
heapq.heapify(col)

answer = 0
while row or col:
    if row and col:
        if row[0][0] > col[0][0]:
            answer = max(answer, col[0][0])
            tmp = [(r[0] - board[r[1]][col[0][1]], r[1]) for r in row]
            heapq.heapify(tmp)
            row = tmp
            heapq.heappop(col)
        else:
            answer = max(answer, row[0][0])
            tmp = [(c[0] - board[row[0][1]][c[1]], c[1]) for c in col]
            heapq.heapify(tmp)
            col = tmp
            heapq.heappop(row)
    else:
        if row:
            answer = max(answer, row[0][0])
            heapq.heappop(row)
        if col:
            answer = max(answer, col[0][0])
            heapq.heappop(col)

print(answer)