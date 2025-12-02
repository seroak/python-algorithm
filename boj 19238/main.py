import sys
from collections import deque

n, m, fuel = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
x, y = map(int, input().split())
passengers = list()
destination = list()
for i in range(m):
    a, b, c, d = map(int, input().split())
    passengers.append([a - 1, b - 1])
    destination.append([c - 1, d - 1])
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

sx, sy = x - 1, y - 1

for _ in range(m):

    # 손님까지의 최단거리 구하기
    queue = deque()
    queue.append([sx, sy])
    visited = [[-1] * n for _ in range(n)]
    visited[sx][sy] = 0
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] != 1 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[cx][cy] + 1
                    queue.append([nx, ny])

    mn = sys.maxsize
    idx = -1
    for i, passenger in enumerate(passengers):
        d = visited[passenger[0]][passenger[1]]
        if d == -1:
            continue
        # 최단거리 갱신
        if d < mn:
            mn = d
            idx = i
        # 최단거리가 같다면 행, 열 순으로 비교
        elif d == mn:
            if passenger[0] < passengers[idx][0] or (
                    passenger[0] == passengers[idx][0] and passenger[1] < passengers[idx][1]):
                idx = i
    if idx == -1:
        print(-1)
        exit(0)

    queue = deque()
    queue.append([passengers[idx][0], passengers[idx][1]])
    visited = [[-1] * n for _ in range(n)]
    visited[passengers[idx][0]][passengers[idx][1]] = 0
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] != 1 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[cx][cy] + 1
                    queue.append([nx, ny])
    # 승객을 태우고 목적지까지 간거리
    dest = visited[destination[idx][0]][destination[idx][1]]
    if dest == -1:
        print(-1)
        exit(0)

    sx, sy = destination[idx][0], destination[idx][1]
    # 승객을 태우는데 연료가 충분해서 성공한 경우
    if dest + mn <= fuel:
        fuel = fuel - (dest + mn) + (2 * dest)
        del passengers[idx]
        del destination[idx]
    # 실패한 경우
    else:
        print(-1)
        exit(0)
print(fuel)
