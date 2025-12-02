n, m = map(int, input().split())
arr = list(map(int, input().split()))
left = 0
right = sum(arr)


# mid 값으로 구슬을 나눴을 떄 3보다 적게 나눠지면 right = mid
# 3보다 많이 나눠지면 left = mid
# 3으로 나눠지면 right = mid
def check(mid):
    tmp = 0
    count = 1
    for i in arr:
        tmp += i
        if tmp > mid:
            tmp = i
            count += 1
            if tmp > mid:
                return False
    if count <= 3:
        return True
    else:
        return False


while left < right:
    mid = (left + right) // 2
    if check(mid):
        right = mid
    else:
        left = mid + 1
min_max_sum = left
print(min_max_sum)

# 최소값 기준으로 실제 그룹 수 생성
count = 1
temp_sum = 0
groups = []
for i in range(n):
    if temp_sum + arr[i] > min_max_sum or (n - i) == (m - count):
        groups.append(i)
        temp_sum = arr[i]
        count += 1
    else:
        temp_sum += arr[i]

# 마지막 그룹 종료
groups.append(n)

# 그룹 크기 출력
sizes = []
prev = 0
for idx in groups:
    sizes.append(idx - prev)
    prev = idx
print(' '.join(map(str, sizes)))
