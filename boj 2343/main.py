n, m = map(int, input().split())
lecture = list(map(int, input().split()))
st = max(lecture)  # 최소 블루레이 크기는 가장 긴 강의 길이 이상
en = sum(lecture)  # 최대 크기는 모든 강의를 하나의 블루레이에 담을 경우
while st < en:

    mid = (st + en) // 2

    tmp = 0
    count = 1
    for i in range(n):
        if tmp + lecture[i] > mid:  # 현재 블루레이에 더 담을 수 없으면
            count += 1  # 새로운 블루레이 필요
            tmp = lecture[i]  # 새 블루레이에 현재 강의 추가
        else:
            tmp += lecture[i]  # 기존 블루레이에 강의 추가

    if count > m:
        st = mid + 1
    else:
        en = mid
print(st)