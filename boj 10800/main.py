n = int(input())
balls = list()
for i in range(n):
    color, size = map(int, input().split())
    balls.append([i, color, size])
balls.sort(key=lambda x: x[2])

colors = [0] * (n + 1)
ans = [0] * (n)
sum_weight = 0
j = 0
for i in range(n):
    while balls[j][2] < balls[i][2]:
        colors[balls[j][1]] += balls[j][2]
        sum_weight += balls[j][2]
        j += 1
    ans[balls[i][0]] = sum_weight - colors[balls[i][1]]


for i in ans:
    print(i)