import heapq
import sys
input = sys.stdin.readline
t = int(input())

def dijkstra(start, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 가장 짧은 거리를 Pop
        dist, now = heapq.heappop(q)
        # 현재 거리가 더 짧으면 다익스트라 돌지 않고 continue
        if distance[now] < dist:
            continue
        for i in graph[now]:
            # 현재 위치에서 해당 좌표까지 걸리는 거리 + 큐에서 뽑은 지금까지 노드가 간 거리 보다 배열에 저장한 거리보다 짧을때
            if dist+i[1] < distance[i[0]]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(q, (dist+i[1], i[0]))
    return distance
for _ in range(t):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[]for _ in range(n+1)]
    st_distance = [sys.maxsize] * (n + 1)
    h_distance = [sys.maxsize] * (n + 1)
    g_distance = [sys.maxsize] * (n + 1)
    cross_cost = 0
    for _ in range(1, m+1):
        st, en, cost = map(int, input().split())
        graph[st].append([en, cost])
        graph[en].append([st, cost])
        if st == g and en == h or st == h and en == g:
            cross_cost = cost

    dest = list()
    for _ in range(t):
        d = int(input())
        dest.append(d)

    st_distance = dijkstra(s, st_distance)
    h_distance = dijkstra(g, h_distance)
    g_distance = dijkstra(h, g_distance)
    print(st_distance)
    print(h_distance)
    print(g_distance)
    answer = list()
    for d in dest:
        if st_distance[d] == h_distance[d] + cross_cost + st_distance[g] or st_distance[d] == g_distance[d] + cross_cost + st_distance[h]:
            answer.append(d)
    answer = sorted(answer)
    print(answer)
    for q in answer:
        print(q, end=" ")
