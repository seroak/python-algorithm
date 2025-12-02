import sys

input = sys.stdin.readline
n = int(input())
ratio = [[] for _ in range(n)]
mass = [0] * n
visited = [False] * n


## 유클리드 호제법
def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


pq_values = []

##관계리스트 생성
common_multi = 1
for _ in range(n-1):
  a, b, p, q = map(int,input().split())
  ratio[a].append([b,p,q])
  ratio[b].append([a,q,p])
  common_multi *= ((p*q)//gcd(p,q))
mass[0] = common_multi



def DFS(r):
    visited[r] = True
    # ratio[0] = 연결된 수, ratio[1] 비율 p, ration[2] 비율 q
    for i in ratio[r]:
        if not visited[i[0]]:
            # mass[r]:mass[i[0] == i[1] : i[2] 라는 비율이므로
            mass[i[0]] = i[2] * mass[r] // i[1]
            DFS(i[0])


DFS(0)
# DFS를 돌고 난후에는 비율에 맞게 나눠진 수들이 나오고 이걸 가장 작게 나누면 된다

greatest_common_divisor = mass[0]
for i in range(1, n):
    greatest_common_divisor = gcd(greatest_common_divisor, mass[i])

for i in range(n):
    print(mass[i] // greatest_common_divisor, end=" ")
