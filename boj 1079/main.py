from collections import deque
n = int(input())
survival = n
crime_score = list(map(int, input().split()))
visited = set()
participant_queue = deque()
for i in range(n):
    participant_queue.append((1<<i, crime_score, n))
    visited.add(i)
board = []
for _ in range(n):
    arr = list(map(int, input().split()))
    board.append(arr)

while participant_queue:
    participant, score, survival = participant_queue.popleft()
    # 밤
    if survival % 2 == 0:
        for i in range(n):
            if participant & (1 << i) == 0:
                new_participant = participant + (1 << i)
                for idx, s in enumerate(board[i]):
                    score[i] += s
                participant_queue.append((new_participant, score, n))
    # 낮
    else:
        for i in range(n):
            if participant & (1 << i) == 0:
                new_participant = participant + (1 << i)

print(4 & (1 << 1))