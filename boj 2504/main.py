pare = input()

stack = list()
tmp = 1
ans = 0
for i in range(len(pare)):
    if pare[i] == "(":
        stack.append("(")
        tmp *= 2
    if pare[i] == "[":
        stack.append("[")
        tmp *= 3

    if pare[i] == ")":
        if len(stack) == 0 or stack[-1] != "(":
            ans = 0
            break

        if pare[i - 1] == "(":
            ans += tmp
        stack.pop()
        tmp //= 2

    if pare[i] == "]":
        if len(stack) == 0 or stack[-1] != "[":
            ans = 0
            break
        if pare[i - 1] == "[":
            ans += tmp
        tmp //= 3
        stack.pop()


if stack:
    ans = 0

print(ans)
