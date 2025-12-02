MOD = 1000007


def DP():
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 0 and j == 0:
                continue
            if board[i][j]:
                for k in range(board[i][j]):
                    for w in range(k + 1):
                        dp[i][j][board[i][j]][w + 1] += dp[i][j - 1][k][w] + dp[i - 1][j][k][w]
                        dp[i][j][board[i][j]][w + 1] %= MOD
            else:
                for k in range(c+1):
                    for w in range(k + 1):
                        dp[i][j][k][w] += dp[i][j - 1][k][w] + dp[i - 1][j][k][w]
                        dp[i][j][k][w] %= MOD


def solution():
    for i in range(c + 1):
        result = 0
        for j in range(c + 1):
            result += dp[n][m][j][i]  # x행, y열, 오락실 중 최대번호 ,방문한 오락실 개수
        result %= MOD
        print(result, end=' ')


n, m, c = map(int, input().split())
dp = [[[[0 for _ in range(c + 1)] for _ in range(c + 1)] for _ in range(m + 1)] for _ in range(n + 1)]
# n행, m열, pc방 인덱스, 지난 pc방 개수
board = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
dp[1][1][0][0] = 1
for i in range(1, c + 1):
    a, b = map(int, input().split())
    if a == 1 and b == 1:
        dp[1][1][0][0] = 0
        dp[1][1][i][1] = 1
    board[a][b] = i
DP()
solution()
