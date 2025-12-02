n = int(input())
decrease = list()
def dfs(num):
    decrease.append(num)
    for i in range(10):
        if num % 10 > i:
            dfs(num * 10 + i)
for i in range(10):
    dfs(i)
decrease.sort()

if n >= len(decrease):
    print(-1)
else:
    print(decrease[n])