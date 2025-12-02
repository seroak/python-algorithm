import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().rstrip()

left = 0
right = 0
ans = 0
# 패턴 생성
while right < m:
    if s[right: right+3] == 'IOI':
        right += 2
        if right - left == 2 * n:
            left += 2
            ans += 1
    else:
        left = right + 1
        right = right + 1

print(ans)