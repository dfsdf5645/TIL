import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    word = input()

    reverse_word = ''
    for i in range(len(word)-1, -1, -1):
        reverse_word += word[i]

    if word == reverse_word:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')