n = int(input())
cities = [list(map(int, input().split())) for _ in range(n)]
visited_all = (1 << n) - 1

INF = float("inf")

cache = [[None] * (1 << n) for _ in range(n)]


def find_path(cur, visited):

    if visited == visited_all:
        return cities[cur][0] or INF
    if cache[cur][visited] is not None:
        return cache[cur][visited]
    tmp = INF
    for city in range(n):
        if (1 << city) & visited == 0 and cities[cur][city]:
            tmp = min(tmp, find_path(city, visited | (1 << city)) + cities[cur][city])
    cache[cur][visited] = tmp
    return cache[cur][visited]


print(find_path(0, 1))

