n = int(input())
arr = list(map(int, input().split()))
dp = list()
dp.append(arr[0])
for i in arr[1:]:
    if dp[-1] < i:
        dp.append(i)
        continue
    st = 0
    en = len(dp)
    mid = 0
    while st < en:
        mid = (st + en) // 2
        if dp[mid] < i:
            st = mid + 1
        else:
            en = mid
    dp[st] = i

print(len(arr) - len(dp))
