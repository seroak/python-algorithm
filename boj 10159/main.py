import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
graph_left = [[] for _ in range(n + 1)]
graph_right = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph_left[b].append(a)
    graph_right[a].append(b)


def dfs_right(node):
    global count
    for i in graph_right[node]:
        if visited_right[i] is True:
            continue
        visited_right[i] = True
        count += 1
        dfs_right(i)


def dfs_left(node):
    global count
    for i in graph_left[node]:
        if visited_left[i] is True:
            continue
        visited_left[i] = True
        count += 1
        dfs_left(i)


for i in range(1, n + 1):
    count = 1
    visited_left = [False for _ in range(n + 1)]
    visited_left[i] = True
    dfs_left(i)
    visited_right = [False for _ in range(n + 1)]
    visited_right[i] = True
    dfs_right(i)
    print(n - count)
