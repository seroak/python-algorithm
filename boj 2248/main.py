answer = ""


def binary(n, m):
    if dp[n][m] != -1:
        return dp[n][m]
    if n == 0 or m == 0:
        dp[n][m] = 1
        return dp[n][m]
    dp[n][m] = binary(n - 1, m) + binary(n - 1, m - 1)

    return dp[n][m]


def make_binary(n, m, nth):
    global answer
    if n == 0:
        return
    if m == 0:
        for i in range(n):
            answer += "0"
        return
    pivot = binary(n - 1, m)
    if nth <= pivot:
        answer += "0"
        make_binary(n - 1, m, nth)
    else:
        answer += "1"
        make_binary(n - 1, m - 1, nth - pivot)


N, M, L = map(int, input().split())

dp = [[-1 for _ in range(M+1)] for _ in range(N+1)]
make_binary(N, M, L)
print(answer)
