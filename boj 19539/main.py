n = int(input())
tree = list(map(int, input().split()))

sum_tree = sum(tree)
if sum_tree % 3 != 0:
    print("NO")
else:
    water = sum_tree // 3
    count = 0
    for t in tree:
        count += t // 2
    if water <= count:
        print("YES")
    else:
        print("NO")