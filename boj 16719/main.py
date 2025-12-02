s = list(input().rstrip())
answer = [""] * len(s)


def pick_priority(st, en):
    idx = st
    char = s[st]

    for i in range(st, en + 1):
        if s[i] < char:
            char = s[i]
            idx = i
    return idx, char


def sol(st, en):
    if st > en:
        return
    idx, char = pick_priority(st, en)
    answer[idx] = char
    print("".join(answer))
    if idx +1 <= en:
        sol(idx + 1, en)
    if idx - 1 >= st:
        sol(st, idx - 1)


sol(0, len(s)-1)
