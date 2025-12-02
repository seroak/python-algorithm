import sys
input = sys.stdin.readline

D, N = map(int, input().split())
oven = list(map(int, input().split()))
pizza = list(map(int, input().split()))
min_o = oven[0]
new_oven = [min_o]
for o in oven[1:]:
    min_o = min(min_o, o)
    new_oven.append(min_o)

pos = D
for p in pizza:
    while pos > 0 and new_oven[pos-1] < p:
        pos -= 1
    if pos <= 0:
        print(0)
        exit(0)
    pos -= 1
print(pos+1)