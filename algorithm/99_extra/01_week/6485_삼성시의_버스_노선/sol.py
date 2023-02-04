import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    result = [0] * (P+1)
    for x in range(P):
        n = int(input())
        for i in range(N):
            if arr[i][0] <= n <= arr[i][1]:
                result[x+1] += 1
    print(f'#{tc}', *result[1:])
