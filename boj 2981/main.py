n = int(input())
number = list()
for i in range(n):
    num = int(input())
    number.append(num)
diff = list()
for i in range(len(number) - 1):
    diff.append(abs(number[i] - number[i + 1]))


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


g = diff[0]
for i in diff[1:]:
    g = gcd(g, i)
ans = list()
for i in range(2, g + 1):
    if g % i == 0:
        ans.append(i)
print(*ans)
