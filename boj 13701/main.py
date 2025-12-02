s = set()
n = list(map(int, input().split()))
for i in n:
    if i not in s:
        s.add(i)
        print(i, end=" ")