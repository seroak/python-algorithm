import sys
from collections import defaultdict

input = sys.stdin.readline
n, k = map(int, input().split())
numbers = defaultdict(int)
for i in range(n):
    number = list(map(str, input().rstrip()))
    number = set(number)
    number = sorted(list(number))
    key = "".join(number)
    numbers[key] += 1
numbers_list = list()
for key, item in numbers.items():
    numbers_list.append([key, item])

answer = 0
for i in range(len(numbers_list)):
    key, count = numbers_list[i]

    key = list(key.rstrip())

    if len(key) == k and 1 < count:
        answer += ((count-1) * (1 + (count-1))) // 2

    for j in range(i+1, len(numbers_list)):
        key_2, count_2 = numbers_list[j]
        # 안쪽 키 set
        key_2 = set(list(key_2.rstrip()))
        # 바깥쪽키 set
        key = set(key)
        result_key = key_2 | key
        if len(result_key) == k:
            answer += count * count_2
print(answer)
