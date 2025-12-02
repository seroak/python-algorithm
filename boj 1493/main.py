l, w, h = map(int, input().split())
n = int(input())
cube = [list(map(int, input().split())) for _ in range(n)]
cube.sort(reverse=True)
volume = l * w * h
before = 0
ans = 0
c = 0
for i, cnt in cube:
    before <<= 3
    v = 2 ** i
    max_cnt = (l // v) * (w // v) * (h // v) - before
    max_cnt = min(max_cnt, cnt)
    before += max_cnt
    ans += max_cnt
    c += max_cnt * v * v * v

if volume == before:
    print(ans)
else:
    print(-1)