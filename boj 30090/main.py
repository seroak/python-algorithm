import sys

input = sys.stdin.readline

n = int(input())
virus = [input().strip() for _ in range(n)]

# 1. 모든 문자열 쌍의 최대 중첩 길이를 미리 계산
overlap = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        s1 = virus[i]
        s2 = virus[j]

        max_k = 0
        # s1의 접미사와 s2의 접두사가 얼마나 겹치는지 확인
        for k in range(min(len(s1), len(s2)), 0, -1):
            if s1.endswith(s2[:k]):
                max_k = k
                break
        overlap[i][j] = max_k

# 최대 중첩 길이 (최적해)
max_total_overlap = 0


# 2. DFS 재설계
def dfs(depth, prev_idx, current_overlap, visited):
    global max_total_overlap

    # 모든 바이러스를 다 사용한 경우
    if depth == n:
        max_total_overlap = max(max_total_overlap, current_overlap)
        return

    # 다음에 올 바이러스를 선택
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            # prev_idx -> i 로 이어붙일 때의 중첩 길이를 더해서 재귀 호출
            dfs(depth + 1, i, current_overlap + overlap[prev_idx][i], visited)
            visited[i] = False


# 3. 모든 바이러스로 시작하는 경우를 탐색
total_len = sum(len(v) for v in virus)
visited = [False] * n

for i in range(n):
    visited[i] = True
    dfs(1, i, 0, visited)
    visited[i] = False

# 4. 최종 결과 계산 및 출력
print(total_len - max_total_overlap)