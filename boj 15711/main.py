t = int(input())
n = 2 * (10 ** 6)
a = [True] * (n + 1)
a[0] = False
a[1] = False
for i in range(2, int(n ** 0.5) + 1):
    if a[i] is True:
        for j in range(i * 2, n + 1, i):
            a[j] = False
prime = [i for i in range(2, n) if a[i]]

for _ in range(t):
    a, b = map(int, input().split())
    # a + b가 4보다 작으면 소수 두개로 나눌 수 없다
    if a + b < 4:
        print("NO")
    # 골든버그 추측에 의해 짝수면 소수 두개로 나눌 수 있다
    elif not (a + b) % 2:
        print("YES")
    elif n < a + b - 2:
        for p in prime:
            if not (a + b - 2) % p:
                print("NO")
                break
        else:
            print("YES")
    else:
        if a + b - 2 in prime:
            print("YES")
        else:
            print("NO")
