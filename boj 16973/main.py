
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))
h, w, sr, sc, fr, fc = map(int, input().split())
visited = [[0 for _ in range(m+1)] for _ in range(n+1)]
psum = [[0 for _ in range(m+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        psum[i][j] = psum[i-1][j]+psum[i][j-1]-psum[i-1][j-1]+a[i-1][j-1]
print(psum)