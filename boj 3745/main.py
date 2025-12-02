while True:
    try:
        n = int(input())
        arr = list(map(int, input().split()))
        order = []
        for target in arr:
            if len(order) == 0 or order[-1] < target:
                order.append(target)
                continue
            left = 0
            right = len(order) - 1
            while left < right:
                mid = (left + right) // 2
                if order[mid] >= target:
                    right = mid
                if order[mid] < target:
                    left = mid + 1
            order[left] = target

        print(len(order))
    except Exception:
        exit(0)