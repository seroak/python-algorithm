from collections import defaultdict

n, d, k, c = map(int, input().split())
sushi = list()
for _ in range(n):
    tmp = int(input())
    sushi.append(tmp)
sushi = sushi + sushi[:k - 1]

eat = set()
count_dict = defaultdict(int)

for i in range(k):
    eat.add(sushi[i])
    count_dict[sushi[i]] += 1

eat.add(c)

mx = len(eat)
left = 0
right = k

while right < len(sushi):
    # 스시 더하기
    count_dict[sushi[right]] += 1
    eat.add(sushi[right])
    # 이전 초밥 제거
    count_dict[sushi[left]] -= 1
    if count_dict[sushi[left]] == 0:
        eat.discard(sushi[left])  # discard 사용 (KeyError 방지)
    # 쿠폰으로 먹는 경우
    eat.add(c)
    mx = max(mx, len(eat))

    right += 1
    left += 1
print(mx)