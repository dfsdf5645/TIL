score = {
    'python': 80,
    'django': 89,
    'web': 83
}

score['algorithm']=90 #항목추가
print(score)
score['python']=85 #값 재할당
score.update({'python':85}) #한번에 여러개 바꾸려고 할 때 update 함수 사용
#score.update({'python':85, 'django':90})

#1.score가 가진 모든 값 순회
#2.그 값들을 어떤 변수에 계속 더해 총합 구함
#3.score 전체 길이 구해 나눔
    #3-1.순회시마다 1씩 커지는 변수
total = 0
lenth = 0
#dict 순회시 key 순회
for key in score:
    print(score[key]) #score['python']
    total += score[key]
    lenth = lenth + 1
# 모든 순회가 다 끝나고 난 뒤,
print(total/lenth)

#초간단 방법
# print(sum(score.values() / len(score.values())))


