import sys
import heapq

n, m = map(int, input().split())
school = list(map(str, input().split()))
graph = [[] for _ in range(n + 1)]
school = [0] + school
queue = list()
for _ in range(m):
    u, v, d = map(int, input().split())
    queue.append([d, u, v])

queue = sorted(queue)
parent = [i for i in range(n + 1)]


def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


answer = 0
for d, u, v in queue:
    if school[u] == school[v]:
        continue
    if find_parent(u) == find_parent(v):
        continue
    union(u, v)
    answer += d

tmp = find_parent(1)
for i in range(2, n+1):
    num = find_parent(i)
    if tmp != num:
        print(-1)
        break
    else:
        tmp = num
else:
    print(answer)