n = int(input())
arr = list(map(int, input().split()))
arr.sort()
k = -1
dict = dict()
for i in arr:
    if i <= 0:
        k += 1
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1


ans = 0
for i in range(k+1):
    left = i + 1
    right = n - 1
    while left < right:
        if arr[i] + arr[left] + arr[right] == 0:
            if arr[left] != arr[right]:
                ans += dict[arr[right]]
            else:
                ans += right - left
            left += 1
        elif arr[i] + arr[left] + arr[right] < 0:
            left += 1
        else:
            right -= 1
print(ans)