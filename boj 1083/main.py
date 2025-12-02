n = int(input())
a = list(map(int, input().split()))
s = int(input())
for i in range(n):
    max_pos = i
    for j in range(i + 1, min(n, i + s+1)):
        if a[max_pos] < a[j]:
            max_pos = j
    while 0 < s and max_pos != i:
        a[max_pos], a[max_pos - 1] = a[max_pos - 1], a[max_pos]
        max_pos -= 1
        s -= 1
print(*a)