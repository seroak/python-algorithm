a = input()
b = input()
rome_num = {"I": 1, 1: "I", "V": 5, 5: "V", "X": 10, 10: "X", "L": 50, 50: "L", "C": 100, 100: "C", "D": 500, 500: "D",
            "M": 1000, 1000: "M"}

a_idx = 0
s = 0
while a_idx < len(a):
    if a_idx != len(a) - 1 and rome_num[a[a_idx]] < rome_num[a[a_idx + 1]]:
        s += rome_num[a[a_idx + 1]] - rome_num[a[a_idx]]
        a_idx += 2
        continue
    s += rome_num[a[a_idx]]
    a_idx += 1


b_idx = 0
q = 0
while b_idx < len(b):
    if b_idx != len(b) - 1 and rome_num[b[b_idx]] < rome_num[b[b_idx + 1]]:
        q += rome_num[b[b_idx + 1]] - rome_num[b[b_idx]]
        b_idx += 2
        continue
    q += rome_num[b[b_idx]]
    b_idx += 1


num = s + q
answer = s + q
rome_number = []


def p_thound(num):
    t = num // 1000
    for _ in range(t):
        rome_number.append("M")
    return num - (t * 1000)


def p_hundred(num):
    h = num // 100
    if h >= 5:
        if h == 9:
            rome_number.append("C")
            rome_number.append("M")
            h -= 9
        else:
            rome_number.append("D")
            h -= 5
    if h == 4:
        rome_number.append("C")
        rome_number.append("D")
        h -= 4
    for _ in range(h):
        rome_number.append("C")
    return num - ((num // 100) * 100)


def p_ten(num):
    t = num // 10
    if t >= 5:
        if t == 9:
            rome_number.append("X")
            rome_number.append("C")
            t -= 9
        else:
            rome_number.append("L")
            t -= 5
    if t == 4:
        rome_number.append("X")
        rome_number.append("L")
        t -= 4
    for _ in range(t):
        rome_number.append("X")
    return num - ((num // 10) * 10)


def p_one(num):
    o = num
    if o >= 5:
        if o == 9:
            rome_number.append("I")
            rome_number.append("X")
            o -= 9
        else:
            rome_number.append("V")
            o -= 5
    if o == 4:
        rome_number.append("I")
        rome_number.append("V")
        o -= 4
    for _ in range(o):
        rome_number.append("I")
    return num - num


if num >= 1000:
    num = p_thound(num)
if num >= 100:
    num = p_hundred(num)
if num >= 10:
    num = p_ten(num)
if num >= 1:
    num = p_one(num)
print(answer)
print("".join(rome_number))