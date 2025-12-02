import sys

input = sys.stdin.readline

N, M, K = map(int, input().strip().split())
answer = ''
dp = [[1 for _ in range(M + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

if dp[N][M] < K:
    print(-1)
    exit(0)

while True:
    if not N:
        answer += "z" * M
        break
    elif not M:
        answer += "a" * N
        break

    temp = dp[N - 1][M]
    if K <= temp:
        answer += "a"
        N -= 1
    else:
        answer += "z"
        M -= 1
        K -= temp

print(answer)
