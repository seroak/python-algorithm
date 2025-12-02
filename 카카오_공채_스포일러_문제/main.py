def solution(message, spoiler_ranges):
    answer = 0
    word_info = []
    word_idx = 0
    for word in message.split(" "):
        word_info.append((word, word_idx, word_idx + len(word)))
        word_idx += len(word) + 1

    spoiler_list = [False] * len(message)
    for start, end in spoiler_ranges:
        for i in range(start, end + 1):
            spoiler_list[i] = True

    reveal_set = set()
    for word, start, end in word_info:
        is_reveal = True
        for i in range(start, end):
            if spoiler_list[i] is True:
                is_reveal = False
                break
        if is_reveal:
            reveal_set.add(word)

    for start, end in spoiler_ranges:
        # 스포방지 삭제
        for i in range(start, end + 1):
            spoiler_list[i] = False
        for word, w_start, w_end in word_info:
            # reveal_set 안에 word가 있는지 없는지 확인
            # 요소가 안에 있으면 확인할 필요가 없다
            # 이미 들어나있는 요소는 중요한 단어가 아니기 때문에
            # 나중에 스포일러 걷어낸 단어도 reveal_set에 넣을 것이기에 중복 체크도 가능하다
            if word in reveal_set:

                continue
            full_reveal = True
            for k in range(w_start, w_end):
                if spoiler_list[k] is True:
                    full_reveal = False
                    break
            # 완전히 들어난 단어가 아니면 넘긴다
            if not full_reveal:
                continue
            # 이번 스포일러를 제거하면서 이번에 모습을 들어내고 중복이 아닌 단어만 검출 된다
            reveal_set.add(word)
            answer += 1

    return answer

message = "here is muzi here is a secret message"
spoiler_ranges = [[0, 3], [23, 28]]
print(solution(message, spoiler_ranges))
message2 = "my phone number is 01012345678 and may i have your phone number"
spoiler_ranges2 = [[5, 5], [25, 28], [34, 40], [53, 59]]
print(solution(message2, spoiler_ranges2))