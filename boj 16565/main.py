import math

MOD = 10007


# 조합 계산 (nCr)


def solve(N):
    total = math.comb(52, N)
    dp = [[0] * (N + 1) for _ in range(14)]
    dp[0][0] = 1

    for i in range(14):  # 1부터 i까지 숫자를 선택하는 경우
        for j in range(N + 1):  # 숫자를 총 몇개 뽑을지
            for k in range(4):  # 현재 단계에서 숫자를 다 뽑은면 안되기 때문에 0~3까지만
                if j >= k:
                    # 이전 숫자까지 선택하고 지금 뽑는 숫자의 차만큼 숫자를 뽑은 경우의수 * 현재 단계 수에서 몇개 뽑을지
                    dp[i][j] += dp[i - 1][j - k] * math.comb(4, k)
                    dp[i][j] = dp[i][j] % MOD

    answer = (total - dp[13][N]) % MOD
    print(answer)


# 입력 및 실행
N = int(input())
solve(N)
