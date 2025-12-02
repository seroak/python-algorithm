c = int(input())
for _ in range(c):
    board = []
    for _ in range(11):
        tmp = list(map(int, input().split()))
        board.append(tmp)

    arrange_board = []
    for i in board:
        tmp = []
        for idx, value in enumerate(i):
            if value != 0:
                tmp.append([idx, value])
        arrange_board.append(tmp)

    unique = set()
    tmp_sum = 0
    answer = 0

    def dfs(depth):
        global tmp_sum
        global answer
        if depth == 11:
            answer = max(answer, tmp_sum)
            return
        for idx, value in arrange_board[depth]:
            if idx not in unique:
                unique.add(idx)
                tmp_sum += value
                dfs(depth + 1)
                tmp_sum -= value
                unique.remove(idx)


    dfs(0)
    print(answer)