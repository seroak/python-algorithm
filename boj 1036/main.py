from collections import defaultdict

to_36_dict = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def switch_36_to_num(s):
    num = 0
    if ord("A") <= ord(s) <= ord("Z"):
        num = ord(s) - ord("A") + 10
    elif 0 <= int(s) <= 9:
        num = int(s)
    return num


def to_36(num):
    if num == 0:
        return "0"
    result = ""
    while num:
        spare = num % 36
        result = to_36_dict[spare] + result
        num = num // 36
    return result


def to_demical(num):
    result = 0
    len_num = len(num)
    for i in range(len_num):
        if ord("A") <= ord(num[i]) <= ord("Z"):
            result += 36 ** (len_num - i - 1) * (ord(num[i]) - ord("A") + 10)
        elif 0 <= int(num[i]) <= 9:
            result += 36 ** (len_num - i - 1) * int(num[i])
    return result


n = int(input())
numbers = []
find_max = defaultdict(int)
for i in range(n):
    number = list(map(str, input()))
    for idx in range(len(number)):
        find_max[str(number[idx])] += (switch_36_to_num("Z") - switch_36_to_num(str(number[idx]))) * (36 ** (len(number) - idx - 1))
    numbers.append(number)

find_max_arr = []
for key, item in find_max.items():
    find_max_arr.append([item, key])
find_max_arr.sort(reverse=True)

k = int(input())
change_z = set()
count = 0
for i in range(k):
    if count == k or i >= len(find_max_arr):
        break
    change_z.add(find_max_arr[i][1])
    count += 1


dem = 0
for strings in numbers:
    tmp_str = strings[:]
    for i in range(len(strings)):
        if strings[i] in change_z:
            tmp_str[i] = "Z"
    q = "".join(tmp_str)
    dem += to_demical(q)

print(to_36(dem))