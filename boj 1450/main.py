import sys

input = sys.stdin.readline


def sum_subset(arr):
    result = list()
    for i in range(1 << len(arr)):
        sub_sum = 0
        is_over = False
        for j in range(len(arr)):
            # 비트가 켜져있는지 확인
            if i & 1 << j:
                sub_sum += arr[j]
                if sub_sum > C:
                    is_over = True
                    break
        if not is_over:
            result.append(sub_sum)
    result.sort()
    return result


N, C = map(int, input().split())
arr = list(map(int, input().split()))
arr1 = arr[:N // 2]
arr2 = arr[N // 2:]

subset1 = sum_subset(arr1)
subset2 = sum_subset(arr2)

pointer1 = 0
pointer2 = len(subset2) - 1
answer = 0
while pointer1 < len(subset1) and 0 <= pointer2:
    if subset1[pointer1] + subset2[pointer2] > C:
        pointer2 -= 1
    else:
        pointer1 += 1
        answer += pointer2 + 1
print(answer)