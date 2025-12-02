def solution(N, M, H, S, C):
    # 사다리 구조 생성
    ladder = [[[False, False] for _ in range(N)] for _ in range(H + 1)]

    # 가로 줄 정보 입력
    for x, y in S:
        x -= 1  # 0-based index
        ladder[y][x][1] = True  # x번째 줄의 오른쪽 연결
        ladder[y][x + 1][0] = True  # x+1번째 줄의 왼쪽 연결

    for i in ladder:
        print(i)
    # 도착점(C)에서 역추적 시작
    cur_pos = C - 1  # 0-based
    cur_height = 0  # 아래(0)에서 시작



    # 아래에서 위로 올라가면서 역추적
    while cur_height < H:
        # 현재 위치와 높이 기록 (1-based)
        path.append(f"{cur_pos + 1} {cur_height}")

        # 다음 높이로 올라가기
        cur_height += 1

        # 현재 높이에서 왼쪽에 가로줄이 있으면 왼쪽에서 왔음
        if ladder[cur_height][cur_pos][0]:
            cur_pos -= 1
        # 오른쪽에 가로줄이 있으면 오른쪽에서 왔음
        elif ladder[cur_height][cur_pos][1]:
            cur_pos += 1


    # 시작 위치 반환 (답)
    answer = cur_pos + 1

    return answer


# 예제 3번 테스트
print("=== 예제 3번 ===")
N = 4
M = 4
H = 10
S = [[1, 7], [3, 6], [1, 5], [2, 8]]
C = 2

print(solution(N, M, H, S, C))




N = 4
M = 3
H = 10
S = [[1, 7], [3, 6], [1, 5]]
C = 2
solution(N, M, H, S, C)