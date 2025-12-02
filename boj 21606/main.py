from collections import deque
import sys
input = sys.stdin.readline

BLACK = "1"
WHITE = "0"

n = int(input())
node_info = [0] + list(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visit = [False for _ in range(n + 1)]
connected_black = [0 for _ in range(n + 1)]
d = deque()

# 실내에서 실외로 가는 경우는 세지 않는다
# 실내에서 실내로 가는 경우와 실외에서 실내로 가는 경우만 센다
# 실외에서 실외로 가는 경우는 큐에 넣고 방문 처리도 해준다
# 1부터 n까지 순회
for check_node in range(1, n + 1):
    # 방문을 했다면 continue
    if visit[check_node]:
        continue
    # 큐에 수를 하나씩 넣는다
    d.append(check_node)
    visit[check_node] = True

    while d:
        # 큐에서 수를 하나 빼고 그 노드가 실외인지 실내인지 체크
        now_node = d.popleft()
        now_color = node_info[now_node]

        # 노드가 실내인 경우
        if now_color == BLACK:
            # 현재 노드하고 연결된 노드를 순회
            for next_node in graph[now_node]:

                # 연결된 노드가 실내인데 아직 방문을 하지 않은 경우
                if node_info[next_node] == BLACK and not visit[next_node]:
                    # 큐에 넣고 방문처리하고 실내와 연결된 경우라고 +1 해준다
                    d.append(next_node)
                    visit[next_node] = True
                    # 맨처음 check_node에 실내하고 연결된 개수를 센다
                    connected_black[check_node] += 1
        # 노드가 실외인경우
        else:
            for next_node in graph[now_node]:
                # 연결된 노드가 실내이고 방문을 하지 않은 경우
                if node_info[next_node] == WHITE and not visit[next_node]:
                    # 큐에넣고 방문 처리
                    d.append(next_node)
                    visit[next_node] = True
                # 실내인 경우는 연결된 노드 +1을 해준다
                elif node_info[next_node] == BLACK:
                    # 맨처음 check_node에 실내하고 연결된 개수를 센다
                    connected_black[check_node] += 1


answer = 0
for node in range(1, n+1):
    if node_info[node] == BLACK:
        answer += (connected_black[node]*2)
    else:
        answer += (connected_black[node] * (connected_black[node]-1))
print(answer)






