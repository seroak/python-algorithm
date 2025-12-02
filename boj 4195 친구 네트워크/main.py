import sys
input = sys.stdin.readline

def find(target):
    if target == parent[target]:
        return target
    parent[target] = find(parent[target])
    return parent[target]
def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    parent[b] = a
    visited[a] += visited[b]

t = int(input())
for _ in range(t):
    f = int(sys.stdin.readline())
    parent = dict()
    visited = dict()

    for i in range(f):
        a, b = map(str, input().split())

        if a not in parent:
            parent[a] = a
            visited[a] = 1

        if b not in parent:
            parent[b] = b
            visited[b] = 1

        union(a, b)
        print(visited[find(a)])