import sys

input = sys.stdin.readline


def dfs(alpha, depth, visited, path):
    if depth == len(alpha):
        print("".join(path))
        return

    prev = set()  # 같은 depth에서 이미 쓴 문자 저장
    for i in range(len(alpha)):
        if not visited[i] and alpha[i] not in prev:
            visited[i] = True
            path.append(alpha[i])
            dfs(alpha, depth + 1, visited, path)
            path.pop()
            visited[i] = False
            prev.add(alpha[i])  # 같은 depth에서 같은 문자 다시 안 쓰게 함


n = int(input())
for _ in range(n):
    alpha = sorted(list(input().strip()))
    visited = [False] * len(alpha)
    dfs(alpha, 0, visited, [])
