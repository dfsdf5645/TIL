import sys
sys.stdin = open('input.txt')

T = int(input())

for case in range(1, T+1):
    N = int(input()) #주어지는 당근 개수
    C = list(map(int, input().split())) #당근 크기

    count = 1
    max_count = 1
    for idx in range(1,N): #0123
        if C[idx-1] < C[idx]:
            count += 1
            if max_count < count:
                max_count = count
        elif C[idx-1] >= C[idx]:
            count = 1


    print(f'#{case} {max_count}')

