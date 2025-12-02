n = int(input())
n -= 1
total_num_len = 0
k = 0
while True:
    total_num_len = (2 * total_num_len) + k + 3
    if n < total_num_len:
        break
    k += 1

while 0 < k:

    mid = k + 3
    side = (total_num_len - mid) // 2
    if 0 <= n < side:
        total_num_len = side
        k -= 1
        continue
    elif side <= n < side + mid:
        n -= side
        break
    elif side + mid <= n < (side * 2) + mid:

        total_num_len = side
        k -= 1
        n -= side + mid
        continue

if n == 0:
    print("m")
else:
    print('o')