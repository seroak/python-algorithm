t = int(input())
for i in range(t):
    n = int(input())
    home = list(map(int, input().split()))
    market = list()
    for _ in range(n):
        market.append(list(map(int, input().split())))
    vis_market = [False for _ in range(len(market))]
    festival = list(map(int, input().split()))
    queue = list()
    queue.append(home)
    flag = False
    while queue:
        x, y = queue.pop()
        if abs(festival[0] - x) + abs(festival[1] - y) <= 1000:
            flag = True
            break
        for idx, item in enumerate(market):
            if vis_market[idx] is True:
                continue
            mx, my = item
            if abs(x - mx) + abs(y - my) <= 1000:
                queue.append([mx, my])
                vis_market[idx] = True
    if flag is True:
        print("happy")
    else:
        print("sad")

