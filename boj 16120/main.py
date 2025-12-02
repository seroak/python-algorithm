ppap = input()
stack = list()
for i in ppap:
    stack.append(i)
    if 4 <= len(stack):
        if stack[-4:] == ['P', 'P', 'A', 'P']:
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()
            stack.append("P")
if len(stack) == 1 and stack[0] == "P":
    print("PPAP")
else:
    print("NP")