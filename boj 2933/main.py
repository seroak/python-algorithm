import sys
from collections import deque

# 왼, 오 순서대로 미네랄을 파괴
    # 미네랄을 파괴하면 그 즉시 탐색 stop
# 파괴 후 클러스터 발생 시(공중에 떠있으면 안됨)
    # - 바닥과 만날 때까지 이동
    # - 또 다른 미네랄을 만날 때 까지 이동

r, c = map(int, sys.stdin.readline().split())
graph = []
for i in range(r):
    temp = sys.stdin.readline()
    temp_list = []
    for j in range(c):
        temp_list.append(temp[j])
    graph.append(temp_list)
cnt = int(sys.stdin.readline()) # 막대 던지는 횟수
hlist = [] # 던지는 위치
hlist = list(map(int, sys.stdin.readline().split()))


def destroy_mi(y, turn): # 미네랄 파괴
    if turn % 2 == 1: # 오른쪽부터
        for i in range(c-1, -1, -1):
            if graph[y][i] == 'x':
                graph[y][i] = '.'
                break
    else: # 왼쪽부터
        for i in range(c):
            if graph[y][i] == 'x':
                graph[y][i] = '.'
                break
    return graph


def find_cluster(graph):
    visit = [[False for x in range(c)] for x in range(r)]
    q = deque()
    for i in range(c):
        if graph[r-1][i] == 'x':
            q.append((r-1, i))
    while q:
        x, y = q.popleft()
        adjlist = [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]
        for nx, ny in adjlist:
            if nx >= 0 and nx < r and ny >= 0 and ny < c:
                if visit[nx][ny] == False:
                    if graph[nx][ny] == 'x':
                        visit[nx][ny] = True
                        q.append((nx, ny))

    cluster = []
    for i in range(r-1, -1, -1):
        for j in range(c):
            if graph[i][j] == 'x' and visit[i][j] == False:
                # 클러스터 발생
                temp = [i, j]
                cluster.append(temp)
    if len(cluster) > 0:
        return cluster, 1, visit  # cluster 있음
    else:
        return cluster, 0, visit  # cluster 없음

def move_cluster(graph, cluster, visit):
    down_min = 1e9
    for x, y in cluster:
        down_cnt = 0
        for i in range(x+1, r):
            if graph[i][y] == '.':
                down_cnt += 1
            if graph[i][y] == 'x' and visit[i][y] == True:
                break
        down_min = min(down_min, down_cnt)
    for x, y in cluster:
        graph[x][y] = '.'
        graph[x+down_min][y] = 'x'
    return graph

for i in range(cnt): # 막대를 던지는 횟수만큼 반복
    # 1) 미네랄 파괴
    graph = destroy_mi(r - hlist[i], i) # 바닥부터 1
    # 2) 클러스터 조사
    cluster, check, visit = find_cluster(graph)

    # 3) 클러스터 이동
    if check == 1:
        graph = move_cluster(graph, cluster, visit)


for i in range(r):
    for j in range(c):
        print(graph[i][j], end = '')
    print()