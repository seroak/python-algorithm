n = input()

numbers = dict()
numbers_set = set()
if len(n) < 10:
    for i in range(1, len(n) + 1):
        numbers[i] = False
        numbers_set.add(i)
else:
    for i in range(1, 10):
        numbers[i] = False
        numbers_set.add(i)
    num = 10
    for i in range(10, len(n), 2):
        numbers[num] = False
        numbers_set.add(num)
        num += 1


answer = []

def dfs(cur):

    if len(numbers_set) == 0:
        print(" ".join(map(str, answer)))
        exit(0)
    for i in range(cur, len(n)):

        if int(n[cur:i+1]) in numbers and numbers.get(int(n[cur:i+1])) is False:
            numbers[int(n[cur:i+1])] = True
            numbers_set.remove(int(n[cur:i+1]))
            answer.append(int(n[cur:i+1]))
            dfs(i+1)
            answer.pop()
            numbers_set.add(int(n[cur:i+1]))
            numbers[int(n[cur:i+1])] = False


dfs(0)
