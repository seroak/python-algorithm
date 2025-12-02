from collections import defaultdict


def combination(n, limit):
    result = []

    def dfs(idx, arr):
        if len(arr) == limit:
            result.append(arr[:])
            return
        for i in range(idx, n):
            arr.append(i)
            dfs(i + 1, arr)
            arr.pop()
        return

    dfs(0, [])
    return result


def product(list, limit):
    result = []

    def dfs(index, arr):
        if limit == len(arr):
            result.append(arr[:])
            return
        for i in list[index]:
            arr.append(i)
            dfs(index + 1, arr)
            arr.pop()

    dfs(0, [])
    return result


def solution(dice):
    answer = 0
    n = len(dice)
    dice_index = [i for i in range(n)]
    max_total = 0
    for choose_dice_idx in combination(n, n // 2):
        total = 0
        choose_dice = [dice[i] for i in choose_dice_idx]
        a_probability = defaultdict(int)
        for arr in product(choose_dice, n // 2):
            a_probability[sum(arr)] += 1

        not_choose_dice_idx = tuple(set(dice_index) - set(choose_dice_idx))
        not_choose_dice = [dice[i] for i in not_choose_dice_idx]
        b_probability = defaultdict(int)
        for arr in product(not_choose_dice, n // 2):
            b_probability[sum(arr)] += 1

        presum = [0] * 501
        for i in range(1, 501):
            presum[i] += presum[i - 1] + b_probability.get(i, 0)
        for k, v in a_probability.items():
            total += presum[k - 1] * v
        if total > max_total:
            max_total = total
            answer = [i+1 for i in choose_dice_idx]
    return answer


dice = [[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]
print(solution(dice))
