n = int(input())
arr = list(map(int, input().split()))
arr.sort()

prefix = 0
for i in arr:
    if prefix + 2 <= i:
        print(prefix+1)
        break
    prefix += i
else:
    print(prefix+1)
