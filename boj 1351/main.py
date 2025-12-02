n, p, q = map(int, input().split())

memo = {0: 1}


def dfs(num):
    if num in memo:
        return memo[num]
    else:
        result = dfs(num // p) + dfs(num // q)
        memo[num] = result
        return result


print(dfs(n))
