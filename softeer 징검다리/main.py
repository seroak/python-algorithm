from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))

stack = []  # LIS 길이를 유지하는 리스트
prev_index = [-1] * n  # 이전 원소의 인덱스를 저장
lis_indices = []  # LIS의 실제 인덱스를 저장

for i in range(n):
    pos = bisect_left(stack, arr[i])  # LIS에서 arr[i]가 들어갈 위치 찾기

    if pos == len(stack):
        stack.append(arr[i])
        lis_indices.append(i)  # 새로운 LIS 요소의 인덱스 저장
    else:
        stack[pos] = arr[i]
        lis_indices[pos] = i  # 해당 위치를 새로운 값으로 교체

    prev_index[i] = lis_indices[pos - 1] if pos > 0 else -1  # 이전 원소의 인덱스 저장
print(prev_index)
print(lis_indices)
# LIS 복원하기
lis_length = len(stack)
lis = [0] * lis_length
current_index = lis_indices[-1]  # LIS 마지막 요소의 인덱스

for i in range(lis_length - 1, -1, -1):
    lis[i] = arr[current_index]
    current_index = prev_index[current_index]

print("LIS 길이:", lis_length)
print("LIS:", lis)