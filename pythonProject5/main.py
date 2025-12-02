# 테스트 케이스의 개수 T를 입력받습니다.
T = int(input())

for test_case in range(1, T + 1):
    # N을 입력받습니다.
    N = int(input())
    # 수열 A를 리스트로 입력받습니다.
    A = list(map(int, input().split()))

    total_sum = 0

    # i는 부분 수열의 시작 인덱스
    for i in range(N):
        current_xor = 0
        # j는 부분 수열의 끝 인덱스
        for j in range(i, N):
            # 이전 XOR 값에 새로운 원소 A[j]를 XOR 연산하여 갱신
            current_xor ^= A[j]
            # 계산된 f(i, j) 값을 총합에 더함
            total_sum += current_xor

    print(f"#{test_case} {total_sum}")