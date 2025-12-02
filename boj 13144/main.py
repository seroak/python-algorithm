from collections import defaultdict, deque


def solution(edges):
    # 그래프 초기화
    graph = defaultdict(list)
    degree = [0 for _ in range(len(graph))]

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        degree[u] += 1
        degree[v] += 1

    # 초기 리프 노드 찾기
    queue = deque(sorted(node for node in graph if degree[node] == 1))
    result = []

    # 위상 정렬
    while queue:
        # 번호가 작은 리프 노드부터 처리
        current = queue.popleft()
        result.append(current)

        # 현재 노드와 연결된 이웃 노드 차수 감소
        for neighbor in graph[current]:
            degree[neighbor] -= 1
            if degree[neighbor] == 1:  # 새롭게 리프 노드가 된 경우
                queue.append(neighbor)

        # 그래프에서 현재 노드 제거
        del graph[current]

        # 큐를 다시 정렬 (번호가 작은 리프 노드부터 처리)
        queue = deque(sorted(queue))

    return result


# 테스트
edges = [[1, 4], [4, 5], [5, 2], [2, 3], [2, 6]]
print(solution(edges))