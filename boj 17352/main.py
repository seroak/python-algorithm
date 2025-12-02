n = int(input())
bridge = []

parent = [i for i in range(n+1)]
def find_parent(a):
    if a != parent[a]:
        parent[a] = find_parent(parent[a])
    return parent[a]
def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
for _ in range(n-2):
    a, b = map(int, input().split())
    union_parent(a, b)
answer = set()
for i in range(1, n+1):
    num=find_parent(i)
    answer.add(num)
print(*answer)
