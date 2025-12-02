r1, c1, r2, c2 = map(int, input().split())
row = abs(r2 - r1) + 1
col = abs(c2 - c1) + 1
arr = [[0 for _ in range(col)] for _ in range(row)]
total = row * col
l = 1
direct = [(0, 1), (-1, 0), (0, -1), (1, 0)]
d = 0
x, y = 0, 0
num = 1

while 0 < total:
    for i in range(2):
        for j in range(l):
            if r1 <= x <= r2 and c1 <= y <= c2:
                arr[x - r1][y - c1] = num
                total -= 1
                m = num
            num += 1
            x += direct[d][0]
            y += direct[d][1]
        d = (d + 1) % 4
    l += 1
max_len = len(str(m))
for i in range(r2-r1+1):
    for j in range(c2-c1+1):
        print(str(arr[i][j]).rjust(max_len), end=" ")
    print()
