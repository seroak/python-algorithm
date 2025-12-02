import math

n, m = map(int, input().split())
graph = [[-1 for _ in range(n)]for _ in range(n)]
for i in range(len(graph)):
    graph[i][i] = 0
node = list()
for i in range(n):
    tmp = list(map(int, input().split()))
    node.append(tmp)
direct = list()
for i in range(m):
    tmp = list(map(int, input().split()))
    direct.append(tmp)

for i in range(len(node)):
    for j in range(i+1, len(node)):
        x1, y1 = node[i]
        x2, y2 = node[j]
        cost = math.sqrt(abs(x2 - x1) ** 2 + abs(y2 - y1) ** 2)
        graph[i][j] = cost


for i in direct:
    x, y = i
    graph[x-1][y-1] = 0
    graph[y-1][x-1] = 0

parent = [i for i in range(n)]

def get_parent(x):
    if x == parent[x]:
        return x
    parent[x] = get_parent(parent[x])
    return parent[x]
def union_parent(a, b):
    a = get_parent(a)
    b = get_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

dist = list()
for i in range(n):
    for j in range(i+1, n):
        dist.append((graph[i][j], i, j))
dist = sorted(dist)

answer = 0
for i in dist:
    cost, a, b = i
    if get_parent(a) != get_parent(b):
        union_parent(a, b)
        answer += cost
print("{:.2f}".format(answer))