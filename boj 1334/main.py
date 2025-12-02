def sol():
    n = int(input())
    num_len = len(str(n))
    if 0 < n < 9:
        print(n + 1)
        return
    all_nine = False
    for i in str(n):
        if i != "9":
            break
    else:
        all_nine = True
    if all_nine:
        print(n + 2)
        return

    # 짝수
    if num_len % 2 == 0:
        n = str(n)
        mid = num_len // 2
        left = n[:mid]
        right = []
        for i in range(mid - 1, -1, -1):
            right.append(left[i])
        pal = left + "".join(right)
        if int(n) >= int(pal):
            left = str(int(left) + 1)
            right = []
            for i in range(mid - 1, -1, -1):
                right.append(left[i])
            pal = left + "".join(right)
        print(pal)
    # 홀수
    else:
        n = str(n)
        mid_idx = (num_len // 2)
        left = n[:mid_idx]
        mid = n[mid_idx]
        right = []
        for i in range(mid_idx - 1, -1, -1):
            right.append(n[i])
        pal = left + mid + "".join(right)
        if int(n) >= int(pal):
            left = n[:mid_idx + 1]
            left = str(int(left) + 1)

            right = []
            for i in range(mid_idx - 1, -1, -1):
                right.append(left[i])
            pal = left + "".join(right)
        print(pal)


sol()
