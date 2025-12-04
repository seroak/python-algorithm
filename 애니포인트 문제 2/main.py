def solution(n, k, bulbs):
    # 1. 색상을 숫자로 변환 (R=0, G=1, B=2)
    maper = {"R": 0, "G": 1, "B": 2}
    arr = [maper[i] for i in bulbs]

    answer = 0
    add_acc = 0
    change_arr = [0] * n

    for i in range(n):
        if i >= k:
            add_acc -= change_arr[i-k]
        arr[i] = (arr[i] + add_acc) % 3
        if arr[i] != 0:
            if i + k > n:
                answer = -1
                break
            cur_change = 3 - arr[i]
            add_acc += cur_change
            change_arr[i] = cur_change
            answer += cur_change

    return answer


n = 6
k = 3
bulbs = "RBGRGB"
print(solution(n, k, bulbs))
