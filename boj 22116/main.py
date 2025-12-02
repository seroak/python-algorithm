import sys
import heapq
input = sys.stdin.readline
n = int(input())
board = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    board.append(tmp)
inf = float("inf")
dist = [[inf] * n for _ in range(n)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
dist[0][0] = 0
heap = []
heapq.heappush(heap, [0, 0, 0])
while heap:
    cost, x, y = heapq.heappop(heap)
    if cost > dist[x][y]:
        continue
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < n and 0 <= ny < n:
            diff = abs(board[x][y] - board[nx][ny])
            cur = max(dist[x][y], diff)
            if cur < dist[nx][ny]:
                dist[nx][ny] = cur
                heapq.heappush(heap, [dist[nx][ny], nx, ny])
print(dist[-1][-1])
