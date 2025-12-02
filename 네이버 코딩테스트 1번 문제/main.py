def survival_probability(revolver, k):
    n = len(revolver)
    doubled = revolver + revolver
    safe_starts = []

    window_sum = sum(doubled[0:k])

    for start in range(n):
        # 마지막 루프에서는 슬라이딩 할 필요 없음
        if window_sum == 0:
            safe_starts.append(start)
        window_sum = window_sum - doubled[start] + doubled[start + k + 1]

    print(safe_starts)
    if len(safe_starts) == 0:
        return 0.0
    print(safe_starts)

    return len(safe_starts) / (len(revolver) - k)


revolver = [1, 1, 0, 0, 0, 0]
k = 2
print(survival_probability(revolver, k))
