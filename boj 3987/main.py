n, m = map(int, input().split())
board = []
for _ in range(n):
    tmp = list(map(str, input().rstrip()))
    board.append(tmp)

pr, pc = map(int, input().split())
dist = None
count = 0
dist_dict = {"U": [-1, 0], "L": [0, -1], "D": [1, 0], "R": [0, 1]}


def decide_dist(dist):
    if dist == 0:
        return "U"
    elif dist == 1:
        return "L"
    elif dist == 2:
        return "D"
    else:
        return "R"


def change45_dist(dist):
    if dist == 'U':
        return "R"
    elif dist == "L":
        return "D"
    elif dist == "D":
        return "L"
    elif dist == "R":
        return "U"


def change315_dist(dist):
    if dist == "U":
        return "L"
    elif dist == "L":
        return "U"
    elif dist == "D":
        return "R"
    elif dist == "R":
        return "D"


answer = -1
answer_dist = None
for i in [0, 3, 2, 1]:
    origin_dist = decide_dist(i)
    dist = decide_dist(i)
    x, y = pr - 1, pc - 1
    count = 0
    is_voyger = False
    visited = set()
    while True:
        x += dist_dict[dist][0]
        y += dist_dict[dist][1]

        count += 1
        if x < 0 or n <= x or y < 0 or m <= y:
            break
        if board[x][y] == "C":
            break

        state = (x, y, dist)
        if state in visited:
            is_voyger = True
            break
        visited.add(state)
        if board[x][y] == "/":
            dist = change45_dist(dist)
        if board[x][y] == "\\":
            dist = change315_dist(dist)
    if is_voyger:
        print(origin_dist)
        print("Voyager")
        exit(0)
    if answer < count:
        answer = count
        answer_dist = origin_dist
print(answer_dist)
print(answer)
