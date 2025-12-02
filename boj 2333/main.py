import math

n = int(input())
primes = [2, 3, 5, 7]


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def dfs(prime, depth):
    for i in range(1, 10):
        if is_prime(prime + i):
            if depth == n-1:
                print(prime + i)
            else:
                if depth < n:
                    dfs((prime + i) * 10, depth + 1)

if n == 1:
    for i in primes:
        print(i)
    exit(0)
for prime in primes:
    dfs(prime * 10, 1)
