import sys


def main():
    input = sys.stdin.readline
    n = int(input())
    arr = list(map(int, input().split()))  # 1-based index 맞추기

    # dp[l][r] = arr[l:r] 구간을 팰린드롬으로 만드는데 필요한 최소 연산
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # 길이가 2 이상인 구간부터 채우기
    for length in range(2, n + 1):  # 부분 수열 길이
        for l in range(0, n - length + 1):
            r = l + length - 1
            if arr[l] == arr[r]:
                dp[l][r] = dp[l + 1][r - 1]
            else:
                dp[l][r] = min(dp[l + 1][r], dp[l][r - 1]) + 1

    print(dp[0][n-1])


if __name__ == "__main__":
    main()