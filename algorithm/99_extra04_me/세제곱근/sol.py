import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ans = round(N**(1/3),2)
    if int(ans) == ans:
        print(f'#{tc} {int(ans)}')
    else:
        print(f'#{tc} -1')