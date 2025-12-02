n = int(input())
arr = list(map(int, input().split()))
stack = list()
stack.append(arr[0])
for i in range(1, n):
    if stack[-1] < arr[i]:
        stack.append(arr[i])
    else:
        st = 0
        en = len(stack)
        target = arr[i]
        while st < en:
            mid = (st + en) // 2
            if stack[mid] < target:
                st = mid + 1
            else:
                en = mid
        stack[st] = target
print(len(stack))