n = int(input())
customers = [list(map(int, input().rstrip())) for _ in range(n)]
visited_all = (1 << n) - 1
cache = [[0] * (1 << n) for _ in range(n)]


def find_customer(cur, visited, cost):
    if cache[cur][visited] != 0:
        return cache[cur][visited]
    tmp = 0
    for customer in range(n):
        if (1 << customer) & visited == 0 and cost <= customers[cur][customer]:
            tmp = max(tmp, find_customer(customer, visited | (1 << customer), customers[cur][customer]) + 1)

    cache[cur][visited] = tmp
    return cache[cur][visited]


print(find_customer(0, 1, 0) + 1)
