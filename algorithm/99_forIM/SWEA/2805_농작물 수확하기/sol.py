import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, list(input().rstrip()))) for _ in range(N)]
    # print(farm)

    n = N // 2
    ans = 0
    for i in range(n+1): #0,1,2
        for j in range(n-i, n+i+1): #2 / 1,2,3 / 0,1,2,3,4
            ans += farm[i][j] + farm[N-i-1][j]
    rlt = ans - sum(farm[n])
    print(f'#{tc} {rlt}')
