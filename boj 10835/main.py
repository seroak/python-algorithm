import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
n = int(input())
left = list(map(int, input().split()))
right = list(map(int, input().split()))
dp = [[-1 for _ in range(n)] for _ in range(n)]


def dfs(left_idx, right_idx):
    if left_idx >= n or right_idx >= n:  # 배열 끝에 도달하면 종료
        return 0
    if dp[left_idx][right_idx] != -1:  # 이미 계산된 값이면 반환
        return dp[left_idx][right_idx]

    # 기본적으로 왼쪽 카드를 버리거나 둘 다 버리는 경우
    dp[left_idx][right_idx] = max(dfs(left_idx + 1, right_idx), dfs(left_idx + 1, right_idx + 1))

    # 오른쪽 카드가 작은 경우 오른쪽 카드 점수를 추가
    if left[left_idx] > right[right_idx]:
        dp[left_idx][right_idx] = max(dp[left_idx][right_idx], dfs(left_idx, right_idx + 1) + right[right_idx])

    return dp[left_idx][right_idx]


dfs(0, 0)
print(dp[0][0])