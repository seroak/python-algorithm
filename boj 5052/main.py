class Trie:
    def __init__(self):
        self.root = {}

    def add(self, numbers):
        cur = self.root
        for num in numbers:
            if num not in cur:
                cur[num] = {}

            cur = cur[num]
        cur["a"] = True

    def travel(self, cur, numbers):
        for num in numbers:
            if "a" in cur:
                return False
            cur = cur[num]
        return True


t = int(input())
for _ in range(t):
    n = int(input())
    trie = Trie()
    numbers_list = list()

    for _ in range(n):
        numbers = tuple(map(int, input().rstrip()))
        trie.add(numbers)
        numbers_list.append(numbers)

    for numbers in numbers_list:
        if trie.travel(trie.root, numbers) is False:
            print("NO")
            break
    else:
        print("YES")
