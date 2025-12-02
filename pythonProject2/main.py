import sys

# 재귀 깊이 제한을 풀어줍니다.
sys.setrecursionlimit(10 ** 6)


# 세그먼트 트리의 노드 값을 계산하는 헬퍼 함수
def get_node_values(val):
    """주어진 값에 대해 (양수 짝수 합, 음수 홀수 합)을 반환합니다."""
    pos_even_sum = 0
    neg_odd_sum = 0
    if val > 0 and val % 2 == 0:
        pos_even_sum = val
    elif val < 0 and val % 2 != 0:
        neg_odd_sum = val
    return (pos_even_sum, neg_odd_sum)


# 세그먼트 트리 구축 함수
def build(tree, arr, node, start, end):
    """세그먼트 트리를 초기 배열 arr로 구축합니다."""
    if start == end:  # 리프 노드
        tree[node] = get_node_values(arr[start])
        return tree[node]

    mid = (start + end) // 2
    left_child = build(tree, arr, node * 2, start, mid)
    right_child = build(tree, arr, node * 2 + 1, mid + 1, end)

    # 자식 노드들의 합으로 부모 노드 값 결정
    tree[node] = (left_child[0] + right_child[0], left_child[1] + right_child[1])
    return tree[node]


# 세그먼트 트리 업데이트 함수
def update(tree, node, start, end, idx, val):
    """idx 위치의 값을 val로 변경하고 트리를 갱신합니다."""
    if start == end:  # 갱신할 리프 노드
        tree[node] = get_node_values(val)
        return

    mid = (start + end) // 2
    if start <= idx <= mid:
        update(tree, node * 2, start, mid, idx, val)
    else:
        update(tree, node * 2 + 1, mid + 1, end, idx, val)

    # 자식 노드가 변경되었으므로 부모 노드 값도 갱신
    left_child = tree[node * 2]
    right_child = tree[node * 2 + 1]
    tree[node] = (left_child[0] + right_child[0], left_child[1] + right_child[1])


# 세그먼트 트리 질의 함수
def query(tree, node, start, end, l, r):
    """[l, r] 범위의 합을 구합니다."""
    # 범위 밖인 경우
    if r < start or end < l:
        return (0, 0)

    # 범위 안에 완전히 포함되는 경우
    if l <= start and end <= r:
        return tree[node]

    # 일부만 겹치는 경우
    mid = (start + end) // 2
    left_result = query(tree, node * 2, start, mid, l, r)
    right_result = query(tree, node * 2 + 1, mid + 1, end, l, r)

    return (left_result[0] + right_result[0], left_result[1] + right_result[1])


# 메인 솔루션 함수
def solution(N, A, Q, Query):
    answer = []

    # 세그먼트 트리는 보통 배열 크기의 4배 정도로 선언합니다.
    # 각 노드는 (pos_even_sum, neg_odd_sum) 튜플을 가집니다.
    tree = [(0, 0)] * (4 * N)

    # 1. 트리 구축
    build(tree, A, 1, 0, N - 1)

    # 2. 쿼리 처리
    for q in Query:
        q_type = q[0]

        if q_type == 1:  # 최대 짝수 합
            L, R = q[1], q[2]
            result = query(tree, 1, 0, N - 1, L, R)
            answer.append(result[0])  # 튜플의 첫 번째 값

        elif q_type == 2:  # 최소 홀수 합
            L, R = q[1], q[2]
            result = query(tree, 1, 0, N - 1, L, R)
            answer.append(result[1])  # 튜플의 두 번째 값

        elif q_type == 3:  # 값 업데이트
            i, C = q[1], q[2]
            update(tree, 1, 0, N - 1, i, C)

    return answer
print(solution(5,[0,0,0,0,0], 7, [[1,0,4], [3,2,3], [1,1,3], [3,1,4], [1,0,4], [3,1,-2],[2,0,4]]))