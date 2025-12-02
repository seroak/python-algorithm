n = int(input())
square = list()
for _ in range(n):
    tmp = list(map(int, input().split()))
    square.append(tmp)
answer = 0
square_idx = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}


def find_max_num(up, down, idx):
    tmp = list()
    for i in range(6):
        if up == i or down == i:
            continue
        tmp.append(square[idx][i])
    return max(tmp)


# 첫번째 상자 아래 위 정하기
for i in range(6):
    up = i
    down = square_idx[up]
    result = 0
    result += find_max_num(up, down, 0)
    # 나머지 상자 순회
    for j in range(1, n):
        up = square[j].index(square[j - 1][down])
        down = square_idx[up]
        result += find_max_num(up, down, j)
    answer = max(result, answer)

print(answer)
