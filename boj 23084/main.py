import sys
input = sys.stdin.readline
S = input().rstrip()
# 원본 비밀번호에 들어있는 수들
max_cnt = [0] * 26

for i in range(len(S)):
    max_cnt[ord(S[i])-ord('a')] += 1

N = int(input())
for n in range(N):
    word = input().rstrip()
    # 비밀번호 후보가 원본 비밀번호보다 작을 때는 가능성이 없으니 바로 NO
    if len(word) < len(S):
        print("NO")
        continue

    word_cnt = [0] * 26
    extra = 0

    left = 0
    right = len(S)-1
    # 처음 슬라이딩으로 비밀번호 후보 길이 만큼 숫자를 표시한다
    # extra는 정답 비밀번호하고 비밀번호 후보하고의 다른 수 차이
    # extra가 1이 돼야한다
    for i in range(right+1):
        num = ord(word[i])-ord('a')
        word_cnt[num] += 1
        # word_cnt는 계속 더하기 때문에 word_cnt가 더 커지는 경우가 생길 것
        # 넘어가면 extra를 +1 한다
        if max_cnt[num] < word_cnt[num]:
            extra += 1
    # 비밀번호 후보의 길이하고 원본 비밀번호의 길이가 같고 extra가 1일 때
    if len(word) == len(S) and extra == 1:
        print('YES')
        continue
    # 비밀번호 후보가 더 길다면 extra 1보다 작아도 된다 다시말해 전부같아도 어차피 그 다음게 다르면 되니까 괜찮다
    # 비밀번호가 abc
    # 비밀번호 후보가 abjk
    # 비밀번호가 처음 초기화 할때 전부 같아도 길이가 후보가 길면 가능인데 길이가 똑같으면 불가능이다
    # 또한 처음 초기화할떄 전부 숫자가 똑같으면 길이가 똑같을때 불가능 이지만 길이가 길면 가능이다
    # 이렇게 둘의 상황이 달라서 if문으로 따로 분리해서 나타낸다
    if len(word) > len(S) and extra <= 1:
        print('YES')
        continue

    while right < len(word)-1:
        # 슬라이딩 윈도우로 왼쪽에 있는 숫자 제거
        left_num = ord(word[left])-ord('a')

        # 후보 비밀번호가 더 크다면 원본 비밀번호와 다른 수가 추가적으로 있는 것 이기에 제거
        if word_cnt[left_num] > max_cnt[left_num]:
            extra -= 1
        word_cnt[left_num] -= 1
        right_num = ord(word[right+1])-ord('a')
        word_cnt[right_num] += 1
        if word_cnt[right_num] > max_cnt[right_num]:
            extra += 1

        if extra <= 1:
            print('YES')
            break

        left += 1
        right += 1

    else:
        print('NO')