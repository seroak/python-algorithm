n, m = map(int, input().split())
spaces = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    tmp_dict = dict()
    sort_tmp = sorted(tmp)

    for idx, i in enumerate(sort_tmp):
        tmp_dict[i] = idx
    order_list = []
    for i in tmp:
        order_list.append(tmp_dict[i])
    spaces.append(order_list)

answer = 0
for i in range(n - 1):
    for k in range(i+1, n):
        for j in range(m):
            if spaces[i][j] != spaces[k][j]:
                break
        else:
            answer += 1
print(answer)
