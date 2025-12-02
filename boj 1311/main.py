n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited_all = (1 << n) - 1
inf = float('inf')
cache = [[inf] * (1 << n) for _ in range(n)]


def find_path(cur, visited):
    if visited == visited_all:
        return 0
    if cache[cur][visited] != inf:
        return cache[cur][visited]
    tmp = inf
    for person in range(n):
        if (1 << person) & visited == 0:
            tmp = min(tmp, find_path(person, visited | (1 << person)) + board[cur][person])
    cache[cur][visited] = tmp
    return tmp


print(find_path(0, 0))
