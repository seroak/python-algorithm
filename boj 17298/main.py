m = int(input())
arr = list(map(int, input().split()))
stack = list()
nge = [-1 for _ in range(m)]
for i in range(len(arr)):
    while stack and arr[i] > arr[stack[-1]]:
        idx = stack.pop()
        nge[idx] = arr[i]
    stack.append(i)
print(*nge)
