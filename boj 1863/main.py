import sys

n = int(sys.stdin.readline())
answer = 0
skylines = []
for i in range(n):
    skylines.append(int(sys.stdin.readline().split()[1]))
skylines.append(0)
# print(skylines)
stk = [0]
for p in skylines:
    height = p
    while stk[-1] > p:
        # print(stk, height)
        if stk[-1] != height:
            # print("카운트 증가")
            answer += 1
            height = stk[-1]
        stk.pop()
    stk.append(p)
print(answer)
