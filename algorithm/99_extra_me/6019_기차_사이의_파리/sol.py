import sys
sys.stdin = open('s_input.txt')

T = int(input())

for case in range(1, T+1):
    D, A, B, F = map(int, input().split())
    result = D / (A + B) * F

    print(f'#{case} {result}')