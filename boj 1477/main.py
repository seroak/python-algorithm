n, m, l = map(int, input().split())  # n, m, l 입력 받음
arr = list(map(int, input().split()))  # 정수 리스트 입력 받음
arr.append(0)
arr.append(l)
arr.sort()


def count_hugeso(mid):
    count = 0
    for i in range(len(arr) - 1):
        gap = arr[i + 1] - arr[i]
        if gap <= 1:
            continue
        count += (gap-1) // mid
    return count


st = 1
en = l
while st < en:
    mid = (st + en) // 2

    # 간격에 따라 휴게소를 세웠는데 휴게소를 더 많이 지었을떄
    if m < count_hugeso(mid):
        # 간격을 더 늘린다
        st = mid + 1
    # 휴게소를 딱 맞게 짓거나 더 적게 지었을떄
    else:
        # 간격을 줄인다
        en = mid
print(st)
