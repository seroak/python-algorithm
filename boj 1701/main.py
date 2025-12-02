import sys
input = sys.stdin.readline
n = str(input())
dp = [[] for _ in range(len(n)+1)]
for k in range(1, len(n)+1):
    flag = False
    for i in range(len(n)+1):
        if i+k > len(n):
            break
        if n[i:i+k] in dp[k]:
            flag = True
        dp[k].append(n[i:i + k])

    if flag is False:
        print(k-1)
        break
