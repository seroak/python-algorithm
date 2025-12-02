n, k = map(int, input().split())
arr = list(map(int, input().split()))
minuse = [arr[i + 1] - arr[i] for i in range(len(arr) - 1)]

minuse.sort()

ans = 0
for i in range((n-1)-(k-1)):
    ans += minuse[i]
print(ans)