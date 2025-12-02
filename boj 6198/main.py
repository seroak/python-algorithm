n = int(input())
building = list()
for i in range(n):
    tmp = int(input())
    building.append(tmp)
dp = [0 for _ in range(n)]
stack = list()
stack.append(building[0])
for i in range(1, n):
    while stack:
        if stack[-1] <= building[i]:
            stack.pop()
        else:
            break
    dp[i] = len(stack)
    stack.append(building[i])
print(sum(dp))
