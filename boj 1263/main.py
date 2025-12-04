n = int(input())
arr = [False] * 1000001
inf = float("inf")
answer = inf
for _ in range(n):
    t, s = map(int, input().split())

    idx = s
    while t:
        if idx < 0:
            answer = -1
            break
        if arr[idx] is False:
            arr[idx] = True
            t -= 1
            idx -= 1
            answer = min(answer, idx)
        else:
            idx -= 1

print(answer)