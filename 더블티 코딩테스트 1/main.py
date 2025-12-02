def calculate_cost(H, target, U, D):
    cost = 0
    for h in H:
        if h < target:
            cost += (target - h) * U
        else:
            cost += (h - target) * D
    return cost


def find_min_cost(N, U, D, H):
    low = min(H)
    high = max(H)
    result = float('inf')

    while low <= high:
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3

        cost1 = calculate_cost(H, mid1, U, D)
        cost2 = calculate_cost(H, mid2, U, D)

        result = min(result, cost1, cost2)

        if cost1 < cost2:
            high = mid2 - 1
        else:
            low = mid1 + 1

    return result


# 입력
N, U, D = map(int, input().split())
H = list(map(int, input().split()))

# 출력
print(find_min_cost(N, U, D, H))