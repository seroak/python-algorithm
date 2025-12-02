def main():
    import sys
    input = sys.stdin.readline
    INF = 10 ** 9

    # 입력: 격자 크기 N, 화살 종류 K, 목표 점수 P
    N, K, P = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    # 화살 i (1 ≤ i ≤ K)를 쏘는 데 필요한 힘(비용); 인덱스 맞추기 위해 앞에 0 추가
    B = [0] + list(map(int, input().split()))

    # possible[i]: 화살 i (사거리 i)로, 발사 위치 (x,y)를 선택했을 때,
    # 맨해튼 거리 < i 인 칸들의 점수 합으로 얻을 수 있는 값들을 모은 집합
    possible = [set() for _ in range(K + 1)]

    for i in range(1, K + 1):
        for x in range(N):
            for y in range(N):
                s = 0
                for a in range(N):
                    for b in range(N):
                        # d < i: 화살 굵기가 1이면 d=0인 자기자신만 포함
                        if abs(a - x) + abs(b - y) < i:
                            s += grid[a][b]
                possible[i].add(s)
        # 중복 제거된 값을 리스트로 변환
        possible[i] = list(possible[i])

    # dp[i][s]: 1번부터 i번 화살까지 고려하여 점수 합 s를 만드는 최소 소비 힘
    dp = [[INF] * (P + 1) for _ in range(K + 1)]

    dp[0][0] = 0

    for i in range(1, K + 1):
        for s in range(P + 1):
            # 화살 i를 사용하지 않는 경우: 이전 dp 값 유지
            if dp[i - 1][s] < INF:
                dp[i][s] = min(dp[i][s], dp[i - 1][s])
                # 화살 i를 사용하는 경우: 가능한 점수값 v 중 하나 선택
                for v in possible[i]:
                    if s + v <= P:
                        dp[i][s + v] = min(dp[i][s + v], dp[i - 1][s] + B[i])
    print(possible)
    for i in dp:
        print(i)
    ans = dp[K][P] if dp[K][P] != INF else -1
    print(ans)


if __name__ == '__main__':
    main()