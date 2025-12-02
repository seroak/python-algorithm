n = int(input())
arr = list(map(str, input().rstrip()))

stack = []
for idx, value in enumerate(arr):
    if stack:
        if stack[-1][1] == "(" and value == ")":
            stack.pop()
        else:
            stack.append([idx, value])
    else:
        stack.append([idx, value])
if len(stack) == 0:
    print(n)
else:
    answer = stack[0][0]
    for i in range(len(stack) - 1):
        answer = max(answer, stack[i + 1][0] - stack[i][0] - 1)
    answer = max(answer, n - 1 - stack[-1][0])
    print(answer)
