T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    answer = sum(arr)
    for i in range(n-1):
        for j in range(i+1, n):
            print(i, j)
            answer += (arr[i] ^ arr[j])
    print(f"#{test_case} {answer}")
print(1^0)
print(1^3)