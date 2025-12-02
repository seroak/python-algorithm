

def solution(category, form, record):
    # Parse category information
    category_info = {}
    for cat in category:
        name, validity = cat.split()
        category_info[name] = int(validity)

    form_info = {}
    for i, info in enumerate(form):
        form_info[i+1] = info.split()

    valid_time = {}
    result = list()
    for rec in record:
        time, form_num = rec.split()
        year, month, day = time.split(".")
        curr_day = int(year)*12*28 + int(month) * 28 + int(day)
        tmp = list()

        for form_name in form_info[int(form_num)]:
            # 이전에 폼을 이용한적 있는지
            if form_name in valid_time:
                # 현재 날짜와 비교해서 유효기간이 남아있다면
                if valid_time[form_name] >= curr_day:
                    tmp.append(form_name)
                else:
                    tmp.append('None')
            else:
                tmp.append('None')
        result.append(tmp)
        for form_name in form_info[int(form_num)]:

            valid_time[form_name] = curr_day + category_info[form_name] * 28
        print(valid_time)
    print(result)
    return


# Test case
category = ["account 1", "address 3", "name 5", "phone 3"]
form = ["name phone", "address name", "account name phone"]
record = ["2010.05.20 1", "2010.08.20 3", "2010.08.28 1", "2011.01.27 2", "2011.04.01 3", "2011.04.28 3"]

print(solution(category, form, record))