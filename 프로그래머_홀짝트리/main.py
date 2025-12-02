from collections import defaultdict


def get_reverse_odd_even_tree(result):
    if (result["reverseOddNode"] == 1 and result["reverseEvenNode"] == 0) or \
            (result["reverseOddNode"] == 0 and result["reverseEvenNode"] == 1):
        return 1
    return 0


def get_odd_even_tree(result):
    if (result["oddNode"] == 1 and result["evenNode"] == 0) or \
            (result["oddNode"] == 0 and result["evenNode"] == 1):
        return 1
    return 0


def explore_tree(tree, visited, result, current):
    nexts = tree[current]
    # 자식이 짝수이고 현재 자신도 짝수이면
    if len(nexts) % 2 == 0 and current % 2 == 0:
        # 홀수 노드
        result["evenNode"] += 1
    # 자식이 홀수이고 현재 자신은 짝수이면
    elif len(nexts) % 2 == 1 and current % 2 == 0:
        # 역 짝수 노드
        result["reverseEvenNode"] += 1
    # 자식이 짝수이고 현재 자신은 홀수이면
    elif len(nexts) % 2 == 0 and current % 2 == 1:
        # 역 홀수 노드
        result["reverseOddNode"] += 1
    # 자식이 홀수이고 현재 자신도 홀수이면
    else:
        # 홀수 노드
        result["oddNode"] += 1
    visited.add(current)
    for nxt in nexts:
        if nxt not in visited:
            explore_tree(tree, visited, result, nxt)


def init_tree(nodes, edges):
    tree = defaultdict(list)
    for node in nodes:
        tree[node] = []
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    return tree


def solution(nodes, edges):
    answer = [0, 0]
    tree = init_tree(nodes, edges)
    visited = set()
    for key in tree.keys():
        if key in visited:
            continue
        result = {"oddNode": 0, "evenNode": 0, "reverseOddNode": 0, "reverseEvenNode": 0}
        explore_tree(tree, visited, result, key)
        print(result)
        answer[0] += get_odd_even_tree(result)
        answer[1] += get_reverse_odd_even_tree(result)
    return answer

nodes = [11, 9, 3, 2, 4, 6]
edges = [[9, 11], [2, 3], [6, 3], [3, 4]]
print(solution(nodes, edges))