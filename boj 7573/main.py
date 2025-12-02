n, l, m = map(int, input().split())
fish = [tuple(map(int, input().split())) for _ in range(m)]

# 좌표 기준 정렬 (y,x)
fish.sort()

answer = 0

# 그물의 세로 길이 h, 가로 길이 w는 l = 2*(h + w)에서 h + w = l // 2
for h in range(1, l // 2):
    w = l // 2 - h
    if w > n - 1 or h > n - 1:
        continue
    print(w, h)
    for i in range(m):
        y, x = fish[i]
        for k in range(w + 1):  # 그물 가로 방향 이동 그물이 왼쪽으로 이동
            cnt = 1
            for j in range(i + 1, m):
                ny, nx = fish[j]
                if ny > y + h:  # 물고기의 y축 위치가 기준으로 잡은 물고기 + 그물높이보다 높으면 나머지도 가망이 없으니 break
                    break
                if x - k <= nx <= x - k + w:
                    cnt += 1
            answer = max(answer, cnt)

print(answer)
