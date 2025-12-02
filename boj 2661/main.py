n = int(input())


def dfs(depth, number):
    if depth == n:
        print(number)
        exit(0)
    for i in range(1, 4):
        tmp_number = number + str(i)
        left = 0
        right = len(tmp_number)
        while left < right:
            if (right - left) % 2 == 1:
                left += 1
                continue
            mid = (left + right) // 2
            if tmp_number[left: mid] == tmp_number[mid: right]:
                break
            left += 1
        else:
            dfs(depth+1, tmp_number)



for i in range(1, 4):
    dfs(1, str(i))
