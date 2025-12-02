from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
K = int(input())
stk = []
for _ in range(K):
    tmp = list(map(int, input().split()))
    for cur, s in [[tmp[0] - 1, 0], [tmp[1] - 1, 1]]:
        while stk and stk[-1][0] < cur:
            stk.pop()
        stk.append([cur, s])
stk.append([-1, -1])

right = stk[0][0]

# 정렬의 영향을 받는 부분을 자른다
sorted_list = deque(sorted(nums[:stk[0][0] + 1]))

for i in range(len(stk)-1):
    cur, s = stk[i]
    nxt, _ = stk[i+1]
    for j in range(cur-nxt):
        if s == 0:
            nums[right] = sorted_list.pop()
        else:
            nums[right] = sorted_list.popleft()
        right -= 1
print(*nums)