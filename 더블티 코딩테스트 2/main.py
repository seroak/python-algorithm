def count_bridges(n, heights):
    stack = []
    count = 0

    for i in range(n):
        while stack and heights[stack[-1]] < heights[i]:
            stack.pop()
        # 같은 높이의 산이 있다면
        if stack and heights[stack[-1]] == heights[i]:

            count += 1
        stack.append(i)
    print(stack)
    return count

# 예제 입력
n = int(input())
heights = list(map(int, input().split()))
print(count_bridges(n, heights))