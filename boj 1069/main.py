X, Y, D, T = map(int, input().split())
dist = (X**2 + Y**2)**0.5 # √(X^2 + Y^2)
answer = float("inf")
jump = dist // D
if dist >= D:
    # 1. 걷기만
    case1 = dist

    # 2. 점프 + 걷기
    case2 = jump * T + (dist - (jump * D))


    # 3. 점프 + 걷기
    case3 = (jump + 1) * T
    answer = min(case1, case2, case3)
else:
    # 1. 걷기만
    case1 = dist
    # 2. 점프 한번 하고 걸어서 돌아가기
    case2 = T + (D-dist)
    # 3. 점프 두번
    case3 = T * 2
    answer = min(case1, case2, case3)
print(answer)
