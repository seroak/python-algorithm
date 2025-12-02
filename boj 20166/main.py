from sys import stdin
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.cnt = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()



    def dfs(self, node, y: int, x: int, cur):
        dy = [1, 1, 0, -1, -1, -1, 0, 1]
        dx = [0, 1, 1, 1, 0, -1, -1, -1]

        if cur == 5:
            return

        # node.children안에 있는 board[y][x]객체를 선택한다
        node = node.children[board[y][x]]
        node.cnt += 1

        for i in range(8):
            ny = (y + dy[i]) % n
            nx = (x + dx[i]) % m
            self.dfs(node, ny, nx, cur + 1)

    # 보드에서 생성 가능한 모든 5글자 문자열을 트라이에 입력
    def insert(self):
        node = self.root

        for i in range(n):
            for j in range(m):
                self.dfs(node, i, j, 0)

    def find(self, word) -> int:
        node = self.root
        for char in word:
            node = node.children[char]
        return node.cnt

    def print_trie(self):
        def dfs_print(node, depth=0, path=""):
            indent = "  " * depth
            print(f"{indent}{path} (cnt: {node.cnt})")
            for char, child in node.children.items():
                dfs_print(child, depth + 1, path + char)

        dfs_print(self.root)


def main():
    def input():
        return stdin.readline().rstrip()

    global n, m, board, trie

    n, m, k = map(int, input().split())
    board = [list(input()) for _ in range(n)]
    trie = Trie()
    # trie.print_trie()

    trie.insert()

    words = [input() for _ in range(k)]

    for word in words:
        print(trie.find(word))


if __name__ == "__main__":
    main()
