import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N, N16 = input().split()

    for i in range(int(N)):
        print(bin(int(N16[i], base=16))[2:].zfill(4), end='')
    print()