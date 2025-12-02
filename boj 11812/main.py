import sys
input = sys.stdin.readline

def getParent(node):
    return ((node-2) // k) + 1
def getDepth(node):
    tmp = 0
    stand = 0
    while True:
        stand += k ** tmp
        if node <= stand:
            return tmp
        tmp += 1
def LCA(a, b):
    global y_depth, x_depth
    mv = 0
    x_parent = a
    y_parent = b
    while True:
        if x_depth == y_depth:
            y_parent = getParent(y_parent)
            x_parent = getParent(x_parent)
            mv += 2
        else:
            if x_depth < y_depth:
                y_parent = getParent(y_parent)
                y_depth -= 1
            else:
                x_parent = getParent(x_parent)
                x_depth -= 1
            mv += 1
        if x_parent == y_parent:
            return mv

n, k, q = map(int, input().split())
for _ in range(q):
    x, y = map(int, input().split())
    x_depth = getDepth(x)
    y_depth = getDepth(y)

    if k == 1:
        print(abs(x-y))
        continue
    print(LCA(x, y))