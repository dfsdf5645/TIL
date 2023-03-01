#swea-learn-course-programming advanced-시작하기-이진수2
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = float(input())      # 부동소수점
    result =''
    while N:
        N *= 2
        if N >= 1:
            N -= 1
            result += '1'
        else:
            result += '0'

    if len(result) >= 13:
        result = 'overflow'
    print(f'#{tc} {result}')