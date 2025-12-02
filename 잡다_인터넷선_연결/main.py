import bisect

def lower_bound(arr, target):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left
def solution(H, W, D):
    answer = 0
    donated_pool = []  # 정렬된 리스트로 관리

    for current_cable in D:
        if current_cable >= H:
            answer += 1
            if current_cable - H > 0:
                idx = lower_bound(donated_pool, current_cable - H)
                donated_pool.insert(idx, current_cable - H)
        else:
            idx = lower_bound(donated_pool, H - current_cable)
            if idx < len(donated_pool):
                answer += 1
                del donated_pool[idx]
            else:
                i = lower_bound(donated_pool, current_cable)
                donated_pool.insert(i, current_cable)
    return answer
H = 5
W = 7
D = [9,7,6,4,3,1]
print(solution(H, W, D))

H = 7
W = 7
D = [11,9,7,2,1,4]
print(solution(H, W, D))