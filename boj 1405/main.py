input_val = list(map(int, input().split()))
n = input_val[0]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
percent = []
for i in range(1, 5):
    percent.append(input_val[i] * 0.01)

visited = [[False] * 31 for _ in range(31)]
answer = 0
def dfs(r, c, idx, probability):
    global answer
    if n == idx:
        answer += probability
        return
    for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]
        if visited[nx][ny] == False:
            visited[nx][ny] = True
            dfs(nx, ny, idx+1, probability * percent[i])
            visited[nx][ny] = False
    return
visited[15][15] = True
dfs(15, 15, 0, float(1))
print(answer)