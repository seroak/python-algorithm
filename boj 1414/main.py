n = int(input())
routes = []
donate = 0
parent = [i for i in range(n)]


def num_parse(num):
    if ord("a") <= ord(num) <= ord("z"):
        return ord(num) - ord("a") + 1
    if ord("A") <= ord(num) <= ord("Z"):
        return ord(num) - ord("A") + 27


def find_parent(a):
    if a != parent[a]:
        parent[a] = find_parent(parent[a])
    return parent[a]
def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a == b:
        return False
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return True
for i in range(n):
    tmp = list(map(str, input().rstrip()))
    for j in range(n):
        line = tmp[j]
        if line == "0":
            continue
        if i == j:
            donate += num_parse(line)
            continue
        routes.append((num_parse(line), i, j))
routes.sort()

for cost, a, b in routes:
    if not union_parent(a, b):
        donate += cost


check = find_parent(0)
for i in range(1, n):
    if check != find_parent(i):
        print(-1)
        break
else:
    print(donate)