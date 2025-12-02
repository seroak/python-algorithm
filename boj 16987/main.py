import sys
input = sys.stdin.readline
n = int(input())
eggs = list()
for _ in range(n):
    egg = list(map(int, input().split()))
    eggs.append(egg)

answer = 0
def dfs(eggs, depth):
    global answer
    # depth는 왼손에 들어야하는 계란
    if depth == n:
        mx = 0

        for egg in eggs:
            if egg[0] <= 0:
                mx += 1
        answer = max(answer, mx)
        return
    if eggs[depth][0] <= 0:
        dfs(eggs, depth + 1)
        return
    flag = False
    # 오른손에 들어야하는 계란 탐색
    for i in range(len(eggs)):
        if i == depth:
            continue
        # 오른손에 들어야하는 계란의 내구도 남아있을때
        if eggs[i][0] > 0:
            flag = True
            new_eggs = [egg[:] for egg in eggs]
            left_dur = new_eggs[depth][0] - new_eggs[i][1]
            right_dur = new_eggs[i][0] - new_eggs[depth][1]
            new_eggs[depth][0] = left_dur
            new_eggs[i][0] = right_dur
            dfs(new_eggs, depth + 1)
    if flag is False:
        dfs(eggs, depth + 1)


dfs(eggs, 0)
print(answer)
