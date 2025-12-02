n = int(input())
food = list(map(int, input().split()))
food.sort()
answer = 0
mod = 1000000007
for i in range(1, len(food)+1):
    answer += food[i-1] * (pow(2,i-1,mod) - pow(2,n-i,mod))
print(answer % mod)
