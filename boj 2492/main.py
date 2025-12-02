n, m, t, k = map(int, input().split())
x_candi = set()
y_candi = set()
stones = []
for _ in range(t):
    x, y = map(int, input().split())
    stones.append((x, y))
    # 원래 후보: x, x-k  -> 경계 안으로 클램프해서 추가
    cx1 = max(0, min(x, n - k))        # stone.x를 왼쪽으로 쓰되 n-k 초과 안되게
    cx2 = max(0, min(x - k, n - k))    # stone.x - k을 왼쪽으로 쓰되 음수 안되게, n-k 초과 안되게
    x_candi.add(cx1)
    x_candi.add(cx2)

    cy1 = max(0, min(y, m - k))
    cy2 = max(0, min(y - k, m - k))
    y_candi.add(cy1)
    y_candi.add(cy2)



answer = -1
a_x = -1
a_y = -1
for x in x_candi:
    for y in y_candi:
        if x + k > n or y + k > m:
            continue
        count = 0
        for stone in stones:
            s_x, s_y = stone
            if x <= s_x <= x + k and y <= s_y <= y + k:
                count += 1
        if answer < count:
            a_x = x
            a_y = y
            answer = count
print(a_x, a_y + k)
print(answer)




