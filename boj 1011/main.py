import math

t = int(input())

for i in range(t):
    s, e = map(int, input().split())
    dis = e - s
    n = int(math.sqrt(dis))

    # 기본 거리
    standard = n * n
    # 기본 이동 횟수
    move = (2 * n) - 1

    # 남은 거리
    remain = dis - standard

    if remain > 0:
        move += 1
        if remain > n:
            move += 1
    print(move)
