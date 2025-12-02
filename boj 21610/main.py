import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
moves = [list(map(int, input().split())) for _ in range(m)]

# 방향 벡터 (8방향)
dist = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
cross = [[-1, -1], [-1, 1], [1, 1], [1, -1]]

# 초기 구름 위치
clouds = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]

for d, s in moves:
    # 구름 이동 후의 위치 저장할 리스트
    new_clouds = []

    # 1. 구름 이동
    for cloud in clouds:
        nx = (cloud[0] + dist[d - 1][0] * s) % n
        ny = (cloud[1] + dist[d - 1][1] * s) % n
        board[nx][ny] += 1
        new_clouds.append((nx,ny))
        # 2. 물 증가


    # 3. 대각선 방향 물 복사
    for cloud in new_clouds:
        count = 0
        for x, y in cross:
            nx, ny = cloud[0] + x, cloud[1] + y
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] > 0:
                count += 1
        board[cloud[0]][cloud[1]] += count

    # 4. 새로운 구름 생성
    clouds = []
    for i in range(n):
        for j in range(n):
            if (i, j) in new_clouds:  # 구름이 있던 자리는 제외
                continue
            if board[i][j] >= 2:
                board[i][j] -= 2
                clouds.append((i, j))  # 새로운 구름 추가

# 최종 합 계산
answer = sum(sum(row) for row in board)
print(answer)