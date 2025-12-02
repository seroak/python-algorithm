n = int(input())  # 노드 개수 입력
arr = list(map(int, input().split()))  # 각 노드의 부모 정보
graph = [[] for _ in range(n)]
root = -1

# 트리 그래프 구성
for i in range(n):
    if arr[i] == -1:
        root = i
    else:
        graph[arr[i]].append(i)

rm = int(input())  # 삭제할 노드 입력

# 루트 노드 자체가 삭제되는 경우 → 결과는 0
if root == rm:
    print(0)
    exit()

answer = 0  # 리프 노드 개수

def dfs(node):
    global answer

    # 현재 노드의 자식 중 `rm`을 제외하고 남은 것이 없다면 리프 노드로 간주
    cnt = 0
    for child in graph[node]:
        if child == rm:
            continue
        dfs(child)
        cnt += 1  # 살아있는 자식 노드 개수 증가

    # 자식이 `rm`뿐이었거나, 아예 없는 경우 리프 노드로 간주
    if cnt == 0:
        answer += 1

dfs(root)
print(answer)