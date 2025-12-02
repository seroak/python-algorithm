import sys

input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
cakes = list()
for i in range(n + 1):
    a, b = map(int, input().split())
    cakes.append([a, b])
dist = [[INF for _ in range(5)] for _ in range(n + 1)]
dist[0] = [1, 1, 1, 1, 0]
dx = [1, 0, -1, 0, 0]
dy = [0, -1, 0, 1, 0]
for i in range(n):
    for j in range(5):
        x, y = cakes[i][0] + dx[j], cakes[i][1] + dy[j]

        for k in range(5):
            ex, ey = cakes[i + 1][0] + dx[k], cakes[i + 1][1] + dy[k]
            dist[i + 1][j] = min(dist[i + 1][j], dist[i][k] + abs(x - ex) + abs(y - ey))

print(min(dist[n]))