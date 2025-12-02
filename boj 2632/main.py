from collections import defaultdict
target = int(input())
m, n = map(int, input().split())
pizza1 = []
pizza2 = []
for _ in range(m):
    p = int(input())
    pizza1.append(p)
for _ in range(n):
    p = int(input())
    pizza2.append(p)
pizza1_combo = defaultdict(int)
pizza2_combo = defaultdict(int)
for p in pizza1:
    pizza1_combo[p] += 1
for p in pizza2:
    pizza2_combo[p] += 1
pizza1_combo[sum(pizza1)] += 1
pizza2_combo[sum(pizza2)] += 1
pizza1_window = len(pizza1)
pizza2_window = len(pizza2)
pizza1 = pizza1 + pizza1
pizza2 = pizza2 + pizza2

for i in range(2, pizza1_window):
    value = sum(pizza1[0:i])
    pizza1_combo[value] += 1
    for left in range(1, pizza1_window):
        right = left + i - 1
        value -= pizza1[left - 1]
        value += pizza1[right]
        pizza1_combo[value] += 1

for i in range(2, pizza2_window):
    value = sum(pizza2[0:i])
    pizza2_combo[value] += 1
    for left in range(1, pizza2_window):
        right = left + i - 1
        value -= pizza2[left - 1]
        value += pizza2[right]
        pizza2_combo[value] += 1

answer = 0
answer += pizza1_combo[target]
answer += pizza2_combo[target]
for key, value in pizza1_combo.items():
    if key == target:
        continue
    if pizza2_combo.get(target - key):
        answer += pizza1_combo[key] * pizza2_combo[target - key]
print(answer)