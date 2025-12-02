def count_equal_partitions(n, a):
    if n < 4:
        return 0

    # 누적 합 배열 생성 (1-based indexing)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + a[i]

    total_sum = prefix_sum[n]

    # 전체 합이 4로 나누어떨어지지 않으면 불가능
    if total_sum % 4 != 0:
        return 0

    target_sum = total_sum // 4

    ans = 0
    count1 = 0  # 누적합이 target_sum인 지점 수
    count2 = 0  # 누적합이 2*target_sum인 지점 수

    for i in range(1, n):
        current_prefix_sum = prefix_sum[i]

        if current_prefix_sum == 3 * target_sum:
            ans += count2
        if current_prefix_sum == 2 * target_sum:
            count2 += count1
        if current_prefix_sum == target_sum:
            count1 += 1
        print(ans, count1, count2)
    return ans


# 📥 표준 입력 처리
if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    print(count_equal_partitions(n, a))