n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
same_a = list()
for i in range(n):
    if a[i] in b:
        same_a.append(a[i])
same_b = list()
for i in range(m):
    if b[i] in a:
        same_b.append(b[i])


ans = list()
while same_a and same_b:
    sorted_a = sorted(same_a, reverse=True)
    sorted_b = sorted(same_b, reverse=True)
    i = 0
    j = 0
    same_num = -1
    while i < len(sorted_a) and j < len(sorted_b):
        if sorted_a[i] == sorted_b[j]:
            ans.append(sorted_a[i])
            same_num = sorted_a[i]
            break
        elif sorted_a[i] < sorted_b[j]:
            j += 1
        else:
            i += 1
    else:
        break

    a_idx = same_a.index(same_num)
    if a_idx+1 >= len(same_a):
        break
    same_a = same_a[a_idx+1:]
    b_idx = same_b.index(same_num)
    if b_idx+1 >= len(same_b):
        break
    same_b = same_b[b_idx+1:]
print(len(ans))
print(*ans)
