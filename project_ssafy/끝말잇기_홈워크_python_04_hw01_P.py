# 끝말잇기 단어의 리스트가 주어졌을 때, 몇 번째 사람이 탈락하는지 확인하는 코드를 작성하시오.
# 조건
# 앞서 입력된 단어의 마지막 문자로 시작하는 단어를 말해야 합니다.
# 끝말잇기를 틀리거나 이전에 등장했던 단어를 사용하는 경우, 지게 됩니다.

words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]

# 빈 리스트
# for 반복 > if 마지막 글자 == 첫글자 & not in 그 리스트
# 리스트에 추가
# else면 {idx}번째가 탈락이라고 하기

word_list = []
for i in range(len(words)-1): #012345
    if words[i][-1] == words[i+1][0] and words[i] not in word_list:
        word_list += [words[i]]
    else:
        print(f'{i+1}번째 사람이 탈락했습니다.')
        break #break 까먹지말기!!!
    i += 1 #이것도 까먹지말기!! if/else다 돌고 +1 해줘야함


# 교수님 답안
# duplicated_word = []
# idx = 0
# while idx < len(words) - 1 :
#     if words[idx][-1] == words[idx + 1][0] and words[idx] not in duplicated_word:
#         duplicated_word += [words[idx]] #리스트로 만들어주면 리스트추가됨 append랑 다른가
#     else:
#         print(f'{idx+1}번째가 탈락했습니다.')
#         break #종료해줌
#     idx += 1
# print(duplicated_word)



