import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def binarysearch(N, key):
    start = 1
    end = N
    cnt = 0
    while start <= end:
        middle = (start+end) // 2
        if middle == key:
            cnt += 1
            return cnt
        elif middle > key:
            end = middle
            cnt += 1
        else:
            start = middle
            cnt += 1

for tc in range(1, T+1):
    P, a, b = map(int, input().split())
    if binarysearch(P, a) < binarysearch(P, b):
        winner = 'A'
    elif binarysearch(P, a) > binarysearch(P, b):
        winner = 'B'
    else:
        winner = 0
    print(f'#{tc} {winner}')