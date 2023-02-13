import sys
sys.stdin = open('input.txt')

def search(word):
    tmp = ''
    #다음조사 대상이 될 문자열을 tmp = ''로 만들어갈거임
    #조사 대상 문자와 조사 대상 다음 문자가
    #같은지를 알아보고
    #같다면 다음 조사 대상에서 두 글자 모두 제외
    #다르면 현재 조사대상인 문자는 다음 조사대상에 포함
    #그리고 조사 대상을 다음칸으로 이동
    idx = 0
    while idx < len(word):
        if word[idx] == word[idx+1]:
            print(word[idx], word[idx+1], True)
            tmp += word[idx+2] #idx, idx+1번째 빼고 전부 추가
            # print(tmp)
            word = tmp
            idx = 0
            tmp = ''
        else:
            tmp += word[idx] #다음 조사 대상에 현재 문자 추가
            idx += 1         #조사 위치 변경
        # print(tmp, idx)
    return word

T = int(input())
for tc in range(1, T+1):
    word = input()
    print(word)
    print(len(search(word))
