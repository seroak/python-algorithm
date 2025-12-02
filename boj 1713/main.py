N = int(input()) # 사진틀 개수
Vote = int(input()) # 총 추천 회수
students = list(map(int, input().split())) # 추천 학생 번호
picture = [] # 사진틀
score = [] # 사진틀 인덱스와 매치해서 추천수 저장할 리스트
for i in range(Vote):
    # 추천받은 학생이 사진틀에 있는 경우
    if students[i] in picture:
        for j in range(len(picture)):
            if picture[j] == students[i]:
                score[j] += 1
    else: # 사진틀에 없고
        if len(picture) >= N: # 사진들 꽉차있으면
            for j in range(N): # 가장 작은 점수 찾고
                if score[j] == min(score):
                    del picture[j]
                    del score[j]
                    break
        picture.append(students[i])  # 새로운거 뒤에 더해줌
        score.append(1)

picture.sort()
print(' '.join(map(str, picture)))