import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    word = input()
    print(f'#{tc} ', end='')
    print(1) if word == ''.join(list(reversed(word))) else print(0)