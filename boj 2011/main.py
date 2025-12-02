n = input()

# 입력 문자열의 길이가 0이면 0 출력
if len(n) == 0:
    print(0)
    exit()

# dp 배열 초기화
dp = [0] * (len(n) + 1)
dp[0] = 1  # 빈 문자열의 디코딩 방법은 1가지
dp[1] = 1  # 한 자리 숫자가 0이 아니면 1가지

# 첫 글자가 0이면 디코딩 불가능
if n[0] == '0':
    print(0)
    exit()

# 동적 프로그래밍으로 디코딩 방법 계산
for i in range(1, len(n)):
    # 한 자리 숫자 경우 (0이 아닌 경우)
    if n[i] != '0':
        dp[i + 1] += dp[i]

    # 두 자리 숫자 경우 (10~26 사이)
    two_digit = int(n[i - 1:i + 1])
    if 10 <= two_digit <= 26:
        dp[i + 1] += dp[i - 1]

    # 1,000,000으로 나눈 나머지 계산
    dp[i + 1] %= 1000000

# 최종 결과 출력
print(dp[len(n)])