from collections import deque

t = int(input())
# 10000 이하 소수 미리 구하기 (에라토스테네스의 체)
prime = [True] * 10001
prime[0] = prime[1] = False
for i in range(2, int(10001 ** 0.5) + 1):
    if prime[i]:
        for j in range(i * i, 10001, i):
            prime[j] = False

for i in range(t):
    a, b = map(int, input().split())
    visited = [False] * 10001
    visited[a] = True
    queue = deque()
    queue.append((a, 0))

    while queue:
        num, cnt = queue.popleft()
        if num == b:

            print(cnt)
            break

        # 일의 자리 변형
        one = num % 10

        for k in range(10):
            tmp = num - one
            tmp += k
            if 1000 <= tmp < 10000 and prime[tmp] is True and visited[tmp] is False:

                visited[tmp] = True
                queue.append((tmp, cnt + 1))
        # 십의 자리 변형
        ten = num % 100
        for k in range(10):
            tmp = num - (ten - one)
            tmp += k * 10
            if 1000 <= tmp < 10000 and prime[tmp] is True and visited[tmp] is False:
                visited[tmp] = True
                queue.append((tmp, cnt + 1))

        # 백의 자리 변형
        hun = num % 1000

        for k in range(10):
            tmp = num - (hun - ten)
            tmp += k * 100
            if 1000 <= tmp < 10000 and prime[tmp] is True and visited[tmp] is False:

                visited[tmp] = True
                queue.append((tmp, cnt + 1))
        # 천의 자리 변형
        thon = num
        for k in range(10):
            tmp = num - (thon - hun)
            tmp += k * 1000

            if 1000 <= tmp < 10000 and prime[tmp] is True and visited[tmp] is False:

                visited[tmp] = True
                queue.append((tmp, cnt + 1))
    else:
        print("Impossible")


