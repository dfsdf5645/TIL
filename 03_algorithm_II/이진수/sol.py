#swea-learn-course-programming advanced-시작하기-이진수
import sys
sys.stdin = open('input.txt')

asc = {hex(i).replace('0x', '').upper(): f'{i:04b}' for i in range(16)}
print(asc)

T = int(input())
for tc in range(1, T+1):
    N, N16 = input().split()

    for i in range(int(N)):
        print(bin(int(N16[i], base=16))[2:].zfill(4))
    print()