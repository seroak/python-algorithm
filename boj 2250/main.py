from collections import deque, defaultdict

n = int(input())
tree = [{"cur": -1, "left": -1, "right": -1} for _ in range(n + 1)]

for _ in range(n):
    a, b, c = map(int, input().split())
    tree[a]["cur"] = a
    tree[a]["left"] = b
    tree[a]["right"] = c

order = defaultdict(int)
level_order = defaultdict(list)
count = 1

possible_root = set(range(1, n + 1))
for node in tree:
    if node["left"] != -1:
        possible_root.discard(node["left"])
    if node["right"] != -1:
        possible_root.discard(node["right"])
root = possible_root.pop()
def inorder(level, node):
    global count
    if tree[node]["left"] != -1:
        inorder(level + 1, tree[node]["left"])

    order[node] = count
    level_order[level].append((node, count))  # ⬅ x좌표 같이 저장
    count += 1

    if tree[node]["right"] != -1:
        inorder(level + 1, tree[node]["right"])


inorder(1, root)

mx = 0
ans_level = 0

for level in level_order:
    positions = [pos for _, pos in level_order[level]]
    gap = max(positions) - min(positions) + 1
    if gap > mx or (gap == mx and ans_level > level):
        mx = gap
        ans_level = level
print(ans_level, mx)