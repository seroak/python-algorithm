N = int(input())
open1, open2 = map(int, input().split())  # 처음에 열려있는 문
order = []  # 열어야 하는 문 저장해둘 리스트
M = int(input())  # 열어야 하는 문 개수
for _ in range(M):
    order.append(int(input()))

# 3차원 dp 선언하기!
# 문에 직접 접근하는 인덱스는 +1 돼있어서 크기를 1씩 늘렸어요.
# M은 열어야 하는 문의 개수라서 그냥 그대로 했어요.
dp = [[[-1] * (N + 1) for _ in range(N + 1)] for _ in range(M)]


def solve(orderIdx, open1, open2):
    if orderIdx == M:
        return 0
    if dp[orderIdx][open1][open2] != -1:
        return dp[orderIdx][open1][open2]
    num1 = solve(orderIdx + 1, order[orderIdx], open2) + abs(order[orderIdx] - open1)
    num2 = solve(orderIdx + 1, open1, order[orderIdx]) + abs(order[orderIdx] - open2)

    result = min(num1, num2)
    dp[orderIdx][open1][open2] = result
    return dp[orderIdx][open1][open2]

print(solve(0, open1, open2))
