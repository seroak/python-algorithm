import sys
input = sys.stdin.readline
n = int(input())
mp, mf, ms, mv = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

mn_cost = float("inf")
ans = list()


def dfs(p, f, s, v, cost, depth, arr):
    global mn_cost
    global ans
    if depth == n:
        if mp <= p and mf <= f and ms <= s and mv <= v:

            if cost < mn_cost or (cost == mn_cost and arr < ans):
                mn_cost = cost
                ans = arr[:]
        return
    arr.append(depth + 1)
    dfs(p + board[depth][0], f + board[depth][1], s + board[depth][2], v + board[depth][3], cost + board[depth][4],
        depth + 1, arr)
    arr.pop()
    dfs(p, f, s, v, cost, depth + 1, arr)


dfs(0, 0, 0, 0, 0, 0, [])
if mn_cost == float("inf"):
    print(-1)
else:
    print(mn_cost)
    print(*ans)
