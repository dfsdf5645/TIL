import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    bstop = [0]*1001
    for _ in range(N):
        X, A, B = map(int, input().split())
        if X == 1:  # 일반 버스
            for i in range(A, B+1):
                bstop[i] += 1
        elif X == 2:    # 급행
            for i in range(A, B, 2):    # A가 짝수면 짝수에 정차, A가 홀수면 홀수에 정차
                bstop[i] += 1
            bstop[B] += 1
        elif X == 3:    # 광역 급행
            bstop[A] += 1
            if A%2==0: # A가 짝수
                for i in range(A+1, B):
                    if i%4==0:
                        bstop[i] += 1
            else:
                for i in range(A+1, B):
                    if i%3==0 and i%10!=0:
                        bstop[i] += 1
            bstop[B] += 1
    maxV = 0
    for i in range(1, 1001):
        if maxV < bstop[i]:
            maxV = bstop[i]
    print(f'#{tc} {maxV}')