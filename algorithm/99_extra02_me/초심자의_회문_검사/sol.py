import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    w = input()
    if w == w[::-1]: # str 거꾸로 출력
        ans = 1
    else:
        ans = 0
    print(f'#{tc} {ans}')
    # word = ''
    # word_reverse = ''
    # for char in w:
    #     word += char
    # for char in w:
    #     word_reverse = char + word_reverse
    # if word == word_reverse:
    #     print(1)
    # else:
    #     print(0)
