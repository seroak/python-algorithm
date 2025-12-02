from collections import deque
board = []
t = int(input())
for i in range(100):
    tmp = list(map(int, input().split()))
    board.append(tmp)

queue = deque()
for idx, i in enumerate(board[-1]):
    if i == 2:
        queue.append([99, idx])
visited = [[False] * 100 for _ in range(100)]
while True:
    x, y = queue.popleft()
    if x == 0:
        print(f"#{1} {y}")
        break
    print(x, y)
    if 0 <= y-1 and board[x][y-1] == 1 and visited[x][y-1] is False:
        visited[x][y-1] = True
        y = y - 1
        queue.append([x, y])
    elif y+1 < 100 and board[x][y+1] and visited[x][y+1] is False:
        visited[x][y+1] = True
        y = y + 1
        queue.append([x, y])
    else:
        visited[x-1][y] = True
        x -= 1
        queue.append([x, y])