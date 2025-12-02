def find_parent(x):
    if parents[x] != x:
        parents[x] = find_parent(parents[x])
    return parents[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break

    roads = list()
    total_cost = 0
    for _ in range(n):
        x, y, z = map(int, input().split())
        roads.append([z, x, y])

        total_cost += z
    roads.sort()

    parents = [i for i in range(m)]
    now_cost = 0
    for z, x, y in roads:
        if find_parent(x) != find_parent(y):
            union_parent(x, y)
            now_cost += z
    print(total_cost - now_cost)
