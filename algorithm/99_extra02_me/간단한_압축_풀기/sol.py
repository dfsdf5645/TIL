import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    zip = ''
    for n in range(N):
        char, num = input().split()
        zip += char * int(num)

    print(f'#{tc}')
    for i in range(0, len(zip), 10):
        print(zip[i:i + 10])