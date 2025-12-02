n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# 3차원 DP 테이블 생성: dp[i][j][k]는 (i,j) 위치에 숫자 k까지 도달했을 때의 최대 경로 길이
dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]

# 초기 조건: 0으로 시작하는 경우만 유효하므로 해당 위치에 1로 세팅
for i in range(n):
    for j in range(n):
        # 0인 곳은 처음으로 시작할 수 있기 때문에 1로 초기화 해준다
        if board[i][j] == 0:
            dp[i][j][0] = 1

# DP 진행
for i in range(n):
    for j in range(n):
        if i == 0 and j > 0:  # 첫 번째 행 (왼쪽에서만 올 수 있음)
            # 이전 열(j-1)의 상태를 그대로 가져옴
            # 처음 초기 값으로 1로 초기화 된 곳이 있을 수 있으니 i,j랑 i,j-1의 최대값을 모두 비교
            for k in range(3):
                dp[i][j][k] = max(dp[i][j][k], dp[i][j - 1][k])

            # 숫자 순서를 따라올 수 있는 경우여서 +1을 해주어야하는 부분 들
            if board[i][j] == 0 and dp[i][j - 1][2]:
                dp[i][j][0] = max(dp[i][j][0], dp[i][j - 1][2] + 1)
            elif board[i][j] == 1 and dp[i][j - 1][0]:
                dp[i][j][1] = max(dp[i][j][1], dp[i][j - 1][0] + 1)
            elif board[i][j] == 2 and dp[i][j - 1][1]:
                dp[i][j][2] = max(dp[i][j][2], dp[i][j - 1][1] + 1)

        elif j == 0 and i > 0:  # 첫 번째 열 (위쪽에서만 올 수 있음)
            for k in range(3):
                dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k])

            if board[i][j] == 0 and dp[i - 1][j][2]:
                dp[i][j][0] = max(dp[i][j][0], dp[i - 1][j][2] + 1)
            elif board[i][j] == 1 and dp[i - 1][j][0]:
                dp[i][j][1] = max(dp[i][j][1], dp[i - 1][j][0] + 1)
            elif board[i][j] == 2 and dp[i - 1][j][1]:
                dp[i][j][2] = max(dp[i][j][2], dp[i - 1][j][1] + 1)

        elif i > 0 and j > 0:  # 일반적인 셀 (위와 왼쪽 둘 다에서 올 수 있음)
            # 이전 경로의 값을 그대로 가져오기
            for k in range(3):
                dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k], dp[i][j - 1][k])

            # 순서에 맞게 이전 값 + 1 갱신
            if board[i][j] == 0:
                if dp[i - 1][j][2]:
                    dp[i][j][0] = max(dp[i][j][0], dp[i - 1][j][2] + 1)
                if dp[i][j - 1][2]:
                    dp[i][j][0] = max(dp[i][j][0], dp[i][j - 1][2] + 1)
            elif board[i][j] == 1:
                if dp[i - 1][j][0]:
                    dp[i][j][1] = max(dp[i][j][1], dp[i - 1][j][0] + 1)
                if dp[i][j - 1][0]:
                    dp[i][j][1] = max(dp[i][j][1], dp[i][j - 1][0] + 1)
            elif board[i][j] == 2:
                if dp[i - 1][j][1]:
                    dp[i][j][2] = max(dp[i][j][2], dp[i - 1][j][1] + 1)
                if dp[i][j - 1][1]:
                    dp[i][j][2] = max(dp[i][j][2], dp[i][j - 1][1] + 1)

# 결과 출력: 도착지점에서의 최대 길이 중 가장 큰 값
print(max(dp[n - 1][n - 1]))