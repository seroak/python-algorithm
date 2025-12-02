def solve():
    import sys
    input = sys.stdin.readline  # 한 줄씩 입력받기
    n, m = map(int, input().split())

    # 각 사람의 CPTI(이진 문자열)를 정수형 비트마스크로 변환하여 빈도수를 센다.
    freq = {}
    for _ in range(n):
        s = input().strip()  # 문자열의 좌우 공백 제거
        mask = int(s, 2)
        if mask in freq:
            freq[mask] += 1
        else:
            freq[mask] = 1
    print(freq)
    # 해밍거리가 1 또는 2가 되는 diff(비트마스크) 목록을 만든다.
    diff_list = []
    # 해밍거리가 1인 경우: 한 비트만 바꾸기
    for i in range(m):
        diff_list.append(1 << i)

    # 해밍거리가 2인 경우: 두 비트를 바꾸기
    for i in range(m):
        for j in range(i + 1, m):
            diff_list.append((1 << i) | (1 << j))

    ans = 0
    # 1. 동일한 CPTI를 가진 사람들끼리 (해밍거리 0)
    for count in freq.values():
        ans += count * (count - 1) // 2

    # 2. 서로 다른 CPTI끼리 (해밍거리 1 또는 2)
    # 중복 계산을 피하기 위해, mask를 오름차순으로 순회하면서 neighbor가 현재 mask보다 큰 경우만 처리한다.
    keys = sorted(freq.keys())
    for mask in keys:
        for d in diff_list:
            neighbor = mask ^ d  # d와 XOR하면 해밍거리가 d에 해당하는 경우의 neighbor mask
            if neighbor > mask and neighbor in freq:
                ans += freq[mask] * freq[neighbor]

    print(ans)


if __name__ == '__main__':
    solve()
