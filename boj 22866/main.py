import sys
input = sys.stdin.readline
n = int(input())
l = list(map(int, input().split()))
stack = []
cnt = [0]*(n+1) # 담겨저있는 탑의 갯수
# [인덱스, 거리 차이]
near = [[int(1e9), int(1e9)] for _ in range(n+1)]

for idx, v in enumerate(l):
    # 스텍에서 현제 높이보다 더 큰것이 나올때까지 pop
    while len(stack) > 0 and stack[-1][1] <= v:
        stack.pop()
    cnt[idx+1] += len(stack)
    if len(stack) > 0:
        # 현재 스택의 idx와 비교하는 idx의 차이
        g = abs(stack[-1][0] - (idx+1))
        # 비교  대상의 거리가 더 짧다면 갱신
        if g < near[idx+1][1]:
            near[idx+1][0] = stack[-1][0]
            near[idx+1][1] = g
        # 거리 차이는 똑같지만 인덱스가 더 작을 때
        elif g == near[idx+1][1] and stack[-1][0] < near[idx+1][0]:
            near[idx+1][0] = stack[-1][0]
    # 스택에는 인덱스와 높이
    stack.append([idx+1, v])
stack = []

for idx, v in reversed(list(enumerate(l))):
    while len(stack) > 0 and stack[-1][1] <= v:
        stack.pop()
    cnt[idx+1] += len(stack)
    if len(stack) > 0:
        g = abs(stack[-1][0] - (idx+1))
        if g < near[idx+1][1]:
            near[idx+1][0] = stack[-1][0]
            near[idx+1][1] = g
        elif g == near[idx][1] and idx+1 < near[idx+1][0]:
            near[idx+1][0] = stack[-1][0]
    stack.append([idx+1, v])

for i in range(1, n+1):
    if cnt[i] == 0:
        print(cnt[i])
    else:
        print(cnt[i], near[i][0])