import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    prev = arr[0]
    count = 1
    tmp = 1
    for i in range(1, N):
        if arr[i] >= prev:
            tmp += 1
            prev = arr[i]
        else:
            prev = arr[i]
            tmp = 1
        if tmp >= count:
            count = tmp
    print(f'#{tc} {count}')