import heapq

n, m, t, d = map(int, input().split())
board = []


def num_parser(chr):
    if ord("A") <= ord(chr) <= ord("Z"):
        return ord(chr) - ord("A")
    if ord("a") <= ord(chr) <= ord("z"):
        return 26 + ord(chr) - ord("a")


def cal_dist(st_i, st_j, en_i, en_j):
    start = board[st_i][st_j]
    end = board[en_i][en_j]
    if start < end:
        return abs(start - end) * abs(start - end)
    else:
        return 1

def reverse_cal_dist(st_i, st_j, en_i, en_j):
    start = board[en_i][en_j]  # ← 반대로
    end = board[st_i][st_j]
    if start < end:  # 원래는 높은 곳으로 이동하는 경우
        return (end - start) * (end - start)
    else:
        return 1



for _ in range(n):
    tmp = list(map(str, input().rstrip()))
    board.append(tmp)

for i in range(len(board)):
    for j in range(len(board[0])):
        board[i][j] = num_parser(board[i][j])

INF = float("inf")
dist_board = [[INF] * m for _ in range(n)]
heap = []
heapq.heappush(heap, [0, 0, 0])
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dist_board[0][0] = 0
while heap:
    dist, r, c = heapq.heappop(heap)
    if dist_board[r][c] < dist:
        continue


    for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if abs(int(board[r][c]) - int(board[nx][ny])) > t:
                continue
            cal_dist_time = cal_dist(r, c, nx, ny)
            if dist_board[r][c] + cal_dist_time > d:
                continue
            if dist_board[nx][ny] > dist_board[r][c] + cal_dist_time:
                dist_board[nx][ny] = dist_board[r][c] + cal_dist_time
                heapq.heappush(heap, [dist_board[r][c] + cal_dist_time, nx, ny])

reverse_dist_board = [[INF] * m for _ in range(n)]

heap = []
heapq.heappush(heap, [0, 0, 0])
reverse_dist_board[0][0] = 0
while heap:
    dist, r, c = heapq.heappop(heap)
    if reverse_dist_board[r][c] < dist:
        continue


    for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]
        if 0 <= nx < n and 0 <= ny < m:

            if abs(int(board[r][c]) - int(board[nx][ny])) > t:
                continue

            cal_dist_time = reverse_cal_dist(r, c, nx, ny)
            if reverse_dist_board[r][c] + cal_dist_time > d:
                continue

            if reverse_dist_board[nx][ny] > reverse_dist_board[r][c] + cal_dist_time:
                reverse_dist_board[nx][ny] = reverse_dist_board[r][c] + cal_dist_time
                heapq.heappush(heap, [reverse_dist_board[r][c] + cal_dist_time, nx, ny])

answer = 0
for i in range(n):
    for j in range(m):
        if dist_board[i][j] + reverse_dist_board[i][j] <= d:
            answer = max(answer, board[i][j])
print(answer)
