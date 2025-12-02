# import sys
#
# input = sys.stdin.readline
# n = int(input())
# arr = list(map(int, input().split()))
# m = int(input())
# tree = [[] for _ in range(4 * n)]
#
# inf = float("inf")
#
#
# def init(st, en, index):
#     if st == en:
#         # [인덱스, 값] 순서로 tree에 저장
#         tree[index] = [st, arr[st]]
#         return [st, arr[st]]
#     mid = (st + en) // 2
#     left_idx, left_val = init(st, mid, 2 * index)
#     right_idx, right_val = init(mid + 1, en, 2 * index + 1)
#     if left_val <= right_val:
#         tree[index] = [left_idx, left_val]
#     else:
#         tree[index] = [right_idx, right_val]
#     return tree[index]
#
#
# def update(st, en, index, target):
#     if target < st or en < target:
#         return tree[index]
#     if st == en:
#         tree[index][1] = arr[target]
#         return tree[index]
#     mid = (st + en) // 2
#     result1 = update(st, mid, index * 2, target)
#     result2 = update(mid + 1, en, index * 2 + 1, target)
#     if result1[1] <= result2[1]:
#         tree[index] = result1
#     else:
#         tree[index] = result2
#
#     return tree[index]
#
# def get(st, en, index, left, right):
#     if en < left or right < st:
#         return [inf, inf]
#     if left <= st and en <= right:
#         return tree[index]
#     mid = (st + en) // 2
#     result1 = get(st, mid, index * 2, left, right)
#     result2 = get(mid + 1, en, index * 2 + 1, left, right)
#     if result1[1] <= result2[1]:
#         return result1
#     else:
#         return result2
#
#
# init(0, n - 1, 1)
#
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     if a == 1:
#         arr[b - 1] = c
#         update(0, n - 1, 1, b - 1)
#
#     elif a == 2:
#         print(get(0, n - 1, 1, b - 1, c - 1)[0] + 1)


class TrieNode:
    __slots__ = ("children", "count")

    def __init__(self):
        self.children = {}
        self.count = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.count += 1  # 여기를 항상 증가

    def min_typing(self, word):
        node = self.root
        length = 0
        for ch in word:
            node = node.children[ch]
            length += 1
            if node.count == 1:
                break
        return length


trie = Trie()

words = ["word", "war", "warrior", "world"]

for w in words:
    trie.insert(w)
def print_trie(node, prefix=""):
    for ch, child in node.children.items():
        print(prefix + ch, child.count)
        print_trie(child, prefix + ch)

print_trie(trie.root)
print(trie.root.count)
print(sum(trie.min_typing(w) for w in words))
