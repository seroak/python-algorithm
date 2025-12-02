from collections import deque

bottles = list(map(int, input().split()))
visited = [[[False] * 201 for _ in range(201)] for _ in range(201)]
queue = deque()
queue.append([0, 0, bottles[2]])
ans = list()
while queue:
    a, b, c = queue.popleft()
    if a == 0:
        ans.append(c)
    # a에 물이 있다면
    if a > 0:
        # a를 b에 부었을 때 넘칠떄
        if a + b > bottles[1]:
            tmp_a = a + b - bottles[1]
            tmp_b = bottles[1]
            if visited[tmp_a][tmp_b][c] is False:
                visited[tmp_a][tmp_b][c] = True
                queue.append([tmp_a, tmp_b, c])
        else:
            tmp_a = 0
            tmp_b = a + b
            if visited[tmp_a][tmp_b][c] is False:
                visited[tmp_a][tmp_b][c] = True
                queue.append([tmp_a, tmp_b, c])
        # a를 c에 부었을 때 넘칠 때
        if a + c > bottles[2]:
            tmp_a = a + c - bottles[2]
            tmp_c = bottles[2]
            if visited[tmp_a][b][tmp_c] is False:
                visited[tmp_a][b][tmp_c] = True
                queue.append([tmp_a, b, tmp_c])
        else:
            tmp_a = 0
            tmp_c = a + c
            if visited[tmp_a][b][tmp_c] is False:
                visited[tmp_a][b][tmp_c] = True
                queue.append([tmp_a, b, tmp_c])
    if b > 0:
        # b를 a에 부었을 때 넘칠때
        if b + a > bottles[0]:
            tmp_b = a + b - bottles[0]
            tmp_a = bottles[0]
            if visited[tmp_a][tmp_b][c] is False:
                visited[tmp_a][tmp_b][c] = True
                queue.append([tmp_a, tmp_b, c])
        # b를 a에 부었을 때 넘치지 않을떄
        else:
            tmp_b = 0
            tmp_a = b + a
            if visited[tmp_a][tmp_b][c] is False:
                visited[tmp_a][tmp_b][c] = True
                queue.append([tmp_a, tmp_b, c])
        # b를 c에 부었을 때 넘칠때
        if b + c > bottles[2]:
            tmp_b = b + c - bottles[2]
            tmp_c = bottles[2]
            if visited[a][tmp_b][tmp_c] is False:
                visited[a][tmp_b][tmp_c] = True
                queue.append([a, tmp_b, tmp_c])
        else:
            tmp_b = 0
            tmp_c = b + c
            if visited[a][tmp_b][tmp_c] is False:
                visited[a][tmp_b][tmp_c] = True
                queue.append([a, tmp_b, tmp_c])
    if c > 0:
        # c를 a에 부었을 때 넘칠때
        if c + a > bottles[0]:
            tmp_c = c + a - bottles[0]
            tmp_a = bottles[0]
            if visited[tmp_a][b][tmp_c] is False:
                visited[tmp_a][b][tmp_c] = True
                queue.append([tmp_a, b, tmp_c])
        else:
            tmp_c = 0
            tmp_a = c + a
            if visited[tmp_a][b][tmp_c] is False:
                visited[tmp_a][b][tmp_c] = True
                queue.append([tmp_a, b, tmp_c])
        # c를 b에 부었을 때 넘칠때
        if c + b > bottles[1]:
            tmp_c = c + b - bottles[1]
            tmp_b = bottles[1]
            if visited[a][tmp_b][tmp_c] is False:
                visited[a][tmp_b][tmp_c] = True
                queue.append([a, tmp_b, tmp_c])
        else:
            tmp_c = 0
            tmp_b = c + b
            if visited[a][tmp_b][tmp_c] is False:
                visited[a][tmp_b][tmp_c] = True
                queue.append([a, tmp_b, tmp_c])
ans = set(ans)
ans = list(ans)
ans.sort()
print(*ans)