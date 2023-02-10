import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    print(f'#{tc}')

    count = 0       # 한 줄에 10글자까지
    idx = 0         # 현재 글자를 얼마나 썼는지
    for word in arr:
        while True:
            print(word[0], end='')  # 글 작성
            count += 1      # 현재 줄에 작성한 글 수
            idx += 1        # 현재 단어 작성한 글 수
            if count == 10: # 현재 줄이 10글자라면
                print()     # 다음줄로 이동
                count = 0   # 0번째 글자부터
            if idx == int(word[1]): # 현재 글자 수를 모두 썼다면
                idx = 0     # 현재 글자수 작성 완료후
                break       # 종료 (다음 글자 작성하러 이동)
    # 다음 tc를 위해 들여쓰기
    print()



