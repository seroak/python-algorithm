from collections import deque
import sys

input = sys.stdin.readline

n, m, p = map(int, input().split())
s = list(map(int, input().split()))
board = [list(input().rstrip()) for _ in range(n)]
answer = [0] * p

# 1) 플레이어별 frontier 큐 초기화
player_queues = [deque() for _ in range(p)]
for i in range(n):
    for j in range(m):
        if board[i][j] not in ('.', '#'):
            pl = int(board[i][j]) - 1
            player_queues[pl].append((i, j))
            answer[pl] += 1

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# 2) 라운드 루프: 한 명이라도 확장 가능하면 계속
while True:
    any_expand = False
    # 플레이어 순회
    for i in range(p):
        # 플레이어가 얼마나 움지여야하는지
        if player_queues[i]:
            move = s[i]
            any_expand = True
            frontier = player_queues[i]
            for _ in range(move):
                next_frontier = deque()
                while frontier:
                    x, y = frontier.popleft()
                    for dx, dy in dirs:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == '.':
                            board[nx][ny] = str(i + 1)
                            answer[i] += 1
                            next_frontier.append((nx, ny))
                if not next_frontier:
                    break
                frontier = next_frontier
            # 이번 턴의 frontier 를 다시 저장
            player_queues[i] = frontier
    if not any_expand:
        break
print(*answer)
