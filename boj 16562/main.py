n, m, k = map(int, input().split())
fee = list(map(int, input().split()))

parent = [i for i in range(n)]


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if fee[a] < fee[b]:
        parent[b] = parent[a]
    else:
        parent[a] = parent[b]


for _ in range(m):
    a, b = map(int, input().split())
    union_parent(a - 1, b - 1)
top_friends = set()
for i in parent:
    top_friends.add(find_parent(i))

ans = 0
for i in top_friends:
    ans += fee[i]

if ans <= k:
    print(ans)
else:
    print("Oh no")
