import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cnts = [0] * 1001
    for i in range(N):
        num, S, E = map(int, input().split())

        if num == 1:    #일반버스
            for j in range(S, E + 1):
                cnts[j] += 1

        elif num == 2:  #급행버스
            if S % 2:   #홀수면
                for k in range(S, E + 1, 2):
                    cnts[k] += 1
            else:
                for l in range(S, E + 1, 2):
                    cnts[l] += 1

        else:           #광역버스
            if S % 2:   #홀수면
                for m in range(S, E + 1):
                    if m % 3 == 0 and m % 10 != 0:
                        cnts[m] += 1
            else:
                for n in range(S, E + 1):
                    if n % 4 == 0:
                        cnts[n] += 1
    print(f'#{tc} {max(cnts)}')
