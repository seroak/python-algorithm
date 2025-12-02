n = int(input())

cnt = 0
ans = list()
def hanoi(n, start, end, sub):
    global cnt
    if n <= 0:
        return
    cnt += 1
    hanoi(n - 1, start, sub, end)
    ans.append([start,end])
    hanoi(n - 1, sub, end, start)


hanoi(n, 1, 3, 2)
print(cnt)
for i in ans:
    print(*i)