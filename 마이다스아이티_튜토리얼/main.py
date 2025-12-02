def solution(X, H, N):
    # 1. 날짜 계산기 설정 (사용자 코드 활용)
    # -----------------------------------------------

    # month[m] = m월 1일 전까지의 누적 일수
    # 예: month[1] = 0, month[2] = 31, month[3] = 59 (31+28)
    month = [0, 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    for i in range(1, len(month)):
        month[i] = month[i] + month[i - 1]

    # (M)월 (D)일을 1년 중 며칠째(day-of-year)인지로 변환
    def get_year_day(d, m):
        return month[m] + d

    def get_month_day(d):
        for i in range(12, 0, -1):
            if d > month[i]:
                return (i, d - month[i])
        return (1, d)

    # 1년 중 (d)번째 날의 요일 계산 (0:월 ~ 5:토, 6:일)
    # [cite_start]문제의 X (1:월 ~ 7:일) [cite: 88]에 맞게 (d-1 + X-1) % 7 사용
    def get_day_of_week(d):
        return (d - 1 + X - 1) % 7

    # 2. 2023년 휴일 배열(holidays) 생성 (사용자 코드 활용)
    # -----------------------------------------------

    # 1년(365일)의 휴일 여부를 저장 (1-indexed)
    holidays = [False] * 366

    # 2-1. 주말(토=5, 일=6)을 휴일로 설정
    for i in range(1, 366):
        if get_day_of_week(i) == 5 or get_day_of_week(i) == 6:
            holidays[i] = True

    # 2-2. 원본 공휴일(H)을 휴일로 설정
    for m, d in H:
        day = get_year_day(d, m)
        if holidays[day] is False:
            holidays[day] = True

    # 2-3. [cite_start]대체 공휴일 규칙 적용 [cite: 32]
    for m, d in H:
        day = get_year_day(d, m)
        week = get_day_of_week(day)

        # [cite_start]규칙 1: 공휴일이 토요일(5)인 경우 -> 이전 평일 [cite: 52, 53]
        if week == 5:
            day -= 1  # 금요일부터 탐색
            while True:
                # [cite_start]규칙 3: 연도를 넘어가면 중단 [cite: 63]
                if day < 1:
                    break
                # 휴일이 아닌 날(평일)을 찾으면 휴일로 지정
                if holidays[day] is False:
                    holidays[day] = True
                    break
                day -= 1  # 이미 휴일이면 하루 더 이전으로

        # [cite_start]규칙 2: 공휴일이 일요일(6)인 경우 -> 이후 평일 [cite: 57, 58]
        if week == 6:
            day += 1  # 월요일부터 탐색
            while True:
                # [cite_start]규칙 3: 연도를 넘어가면 중단 [cite: 63]
                if day > 365:
                    break
                # 휴일이 아닌 날(평일)을 찾으면 휴일로 지정
                if holidays[day] is False:
                    holidays[day] = True
                    break
                day += 1  # 이미 휴일이면 하루 더 이후로
    left = 1
    used_holiday = 0
    max_duration = 0
    start_day = -1
    end_day = -1
    for right in range(1, 366):
        if holidays[right] is False:
            used_holiday += 1
        if used_holiday > N:
            if holidays[left] is False:
                used_holiday -= 1
            left += 1
        if max_duration < right - left + 1:
            max_duration = right - left + 1
            start_day = left
            end_day = right

    start_d, start_m = get_month_day(start_day)
    end_d, end_m = get_month_day(end_day)

    return [max_duration, start_d, start_m, end_d, end_m]


X = 7
H = [[1, 1], [1, 21], [1, 22], [1, 23], [3, 1], [5, 5], [5, 27], [6, 6], [8, 15], [9, 28], [9, 29], [9, 30], [10, 3],
     [10, 9], [12, 25]]
N = 3
print(solution(X, H, N))
