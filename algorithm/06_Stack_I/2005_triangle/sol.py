import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    dp = [[1]*i for i in range(1, N+1)]
    for i in range(2, N):
        for j in range(1, i):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

    print(f'#{tc}')
    for lst in dp:
        print(*lst)
