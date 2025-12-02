import sys
import math

# 입력 파일 읽기 (Linux는 표준 입력, 다른 환경은 파일에서 읽기)
input = sys.stdin.readline

n, attack = map(int, input().split())

answer = 0
injury = 0

for i in range(n):
    t, a, h = map(int, input().split())

    if t == 1:
        atk_cnt = math.ceil(h / attack)
        injury += (atk_cnt - 1) * a
        answer = max(answer, injury)
    elif t == 2:
        attack += a
        if injury < h:
            injury = 0
        else:
            injury -= h

print(answer + 1)
