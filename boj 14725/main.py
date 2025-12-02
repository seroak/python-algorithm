import sys


class Trie:
    def __init__(self):
        self.root = {}

    def add(self, foods):
        cur = self.root

        for food in foods:
            if food not in cur:
                cur[food] = {}  # 자식 노드
            # cur을 자식노드로 교체
            cur = cur[food]
        # foods안에 있는건 전부 문자열이기 때문에 겹칠 걱정은 하지 않아도 된다
        cur[0] = True  # 리프 노드 표시

    def travel(self, level, hall):
        if 0 in hall:
            return

        for i in sorted(hall):
            print("--" * level + i)
            self.travel(level + 1, hall[i])

input = sys.stdin.readline
N = int(input())
trie = Trie()
for i in range(N):
    data = list(input().split())
    trie.add(data[1:])

trie.travel(0, trie.root)
