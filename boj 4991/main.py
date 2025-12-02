import sys
from collections import deque
input = sys.stdin.readline
while True:
    # h * w
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    board = [list(map(str, input().rstrip())) for _ in range(h)]
    start = list()
    dirty = list()

    for i in range(h):
        for j in range(w):
            if board[i][j] == "o":
                start.append(i)
                start.append(j)
            if board[i][j] == "*":
                dirty.append([i, j])

    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    inf = float("inf")
    graph = [[0 for _ in range(len(dirty) + 1)] for _ in range(len(dirty) + 1)]


    def bfs(r, c, st):
        q = deque()
        visited = [[-1 for _ in range(w)] for _ in range(h)]
        visited[r][c] = 0
        q.append([r, c])
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < h and 0 <= ny < w:
                    if board[nx][ny] != "x" and visited[nx][ny] == -1:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append([nx, ny])

        # 시작점에서 더러운 칸 까지의 최소값 갱신
        for i in range(len(dirty)):
            graph[st][i + 1] = visited[dirty[i][0]][dirty[i][1]]


    # 시작위치에서 더러운 칸까지의 최소거리
    bfs(start[0], start[1], 0)
    # 더러운 칸에서 다른 더러운 칸까지의 최소거리
    for i in range(len(dirty)):
        # 더러운 칸의 인덱스는 1부터 시작이니까 i+1
        bfs(dirty[i][0], dirty[i][1], i + 1)

    visited_all = (1 << (len(dirty) + 1)) - 1

    dp = [[inf for _ in range(visited_all + 1)] for _ in range(len(dirty) + 1)]


    # dp[i][j] 현재 i에 있고 j를 방문한 상태에서 나머지 방문 안한 곳을 최소거리로 방문할 수 있는 거리
    def find_path(cur, vis):

        if vis == visited_all:
            dp[cur][vis] = 0
            return 0
        if dp[cur][vis] != inf:
            return dp[cur][vis]
        mn = inf
        for i in range(len(dirty) + 1):
            # 방문을 하지 않았어야한다
            if vis & 1 << i == 0 and graph[cur][i] != 0 and graph[cur][i] != -1:
                mn = min(mn, find_path(i, vis | 1 << i) + graph[cur][i])
        dp[cur][vis] = mn
        return mn


    ans = find_path(0, 1)
    if ans == inf:
        print(-1)
    else:
        print(ans)
