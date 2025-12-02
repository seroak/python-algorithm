n = int(input())
arr = list(map(int, input().split()))
left_sum = list()
left = 0
for i in arr:
    left += i
    left_sum.append(left)

right_sum = list()
right = left_sum[-1]
for i in arr:
    right_sum.append(right)
    right -= i


mx = 0

# 왼쪽
for i in range(1, len(arr) - 1):
    mx = max(mx, (left_sum[-1] - left_sum[i] - arr[i] + left_sum[-1] - left_sum[0]))


for i in range(1, len(arr) - 1):
    mx = max(mx, (right_sum[0] - right_sum[i] - arr[i] + right_sum[0] - right_sum[-1]))

tmp = 0
for i in arr[1:-1]:
    tmp += i
tmp += max(arr[1:-1])
mx = max(mx, tmp)
print(mx)