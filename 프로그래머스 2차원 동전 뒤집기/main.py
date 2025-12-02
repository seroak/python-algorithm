def solution(beginning, target):
    r, c = len(beginning), len(beginning[0])
    answer = float('inf')

    # 행 뒤집기 패턴 완전 탐색
    for row_mask in range(1 << r):
        # 보드 복사
        board = [row[:] for row in beginning]

        # 선택한 행 뒤집기
        for i in range(r):
            if row_mask & (1 << i):
                for j in range(c):
                    board[i][j] ^= 1

        # 선택한 열 뒤집기
        col_mask = 0
        for j in range(c):
            if board[0][j] != target[0][j]:
                col_mask += (1 << j)
                for i in range(r):
                    board[i][j] ^= 1

        if board == target:
            count = bin(row_mask).count("1") + bin(col_mask).count("1")
            answer = min(answer, count)
    return answer if answer != float('inf') else -1


beginning = [[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]
target = [[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]
solution(beginning, target)
