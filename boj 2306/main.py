import sys

input = sys.stdin.readline

# KOI = at, gc
# KOI 유전자 길이 2, 4, 6, 8, ... 는 짝수

myDNA = input().rstrip()
N = len(myDNA)

DP = [[-1] * N for _ in range(N)]  # DP[i][j] = i ~ j 까지 DNA 서열에서 최장KOI 길이


def dfs(st, en):
    if st >= en:
        return 0
    if DP[st][en] != -1:
        return DP[st][en]
    if (myDNA[st] == 'a' and myDNA[en] == 't') or (myDNA[st] == 'g' and myDNA[en] == 'c'):
        DP[st][en] = max(DP[st][en], dfs(st + 1, en - 1) + 2)

    for i in range(st, en):
        DP[st][en] = max(DP[st][en], dfs(st, i) + dfs(i + 1, en))

    return DP[st][en]


dfs(0, len(DP) - 1)
print(DP[0][N - 1])
