import sys

sys.setrecursionlimit(100000)  # 필요한 경우 재귀 한도 증가


def main():
    K = int(input())
    dp = [0] * (K + 1)
    winner = starts_game_with_num(1, K, dp)
    print("Kali" if winner == 1 else "Ringo")



# 1부터 시작해서 k까지 모든 경우를 탐색
def starts_game_with_num(start, K, dp):
    if start >= K:
        return -1

    if dp[start] != 0:
        return dp[start]

    for divisor in find_divisors(start):
        if start + divisor <= K and starts_game_with_num(start + divisor, K, dp) == -1:
            dp[start] = 1
            return dp[start]
    dp[start] = -1
    return dp[start]


def find_divisors(num):
    divisors = []
    for n in range(1, int(num ** 0.5) + 1):
        if num % n == 0:
            divisors.append(n)
            if num // n != n:
                divisors.append(num // n)
    return divisors


if __name__ == "__main__":
    main()
