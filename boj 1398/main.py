t = int(input())
for _ in range(t):
    cost = int(input())
    k = len(str(cost))
    coins = [1, 10, 25]
    answer = 0
    dp =[10**15+1 for _ in range(100)]
    print(dp)