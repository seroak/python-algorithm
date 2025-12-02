n, m = map(int, input().split())
moneys = list()
for _ in range(n):
    q = int(input())
    moneys.append(q)

left = 0
right = sum(moneys) + 1
while left < right:
    mid = (left + right) // 2
    # 인출할 수 있는 돈
    withdraw = mid
    # 현재 가지고 있는 돈
    chash = mid
    # 인출 카운트
    count = 1
    # 인출하는 돈이 money보다는 커야한다
    flag = False
    for money in moneys:
        # 인출하려는 돈이 필요한 돈보다 적을때
        if withdraw < money:
            flag = True
            break
        # 지금 가지고 있는 돈으로 돈을 낼 수 있을 때
        if money <= chash:
            chash -= money

        # 지금 가지고 있는 돈으로 돈을 낼 수 없을때
        else:
            # 돈 인출
            chash = withdraw
            count += 1

            if money <= chash:
                chash -= money

    # 인출한 횟수가 m보다 크거나 필요한 돈보다 인출할 수 있는 돈이 적을 떄

    if m < count or flag is True:
        left = mid + 1
    else:
        right = mid
print(left)
