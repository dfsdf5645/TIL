import sys
sys.stdin = open('input1.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    rms = [list(map(int, input().split())) for _ in range(M)]

    cnt = 1           #가로
    # cnt2 = 1        #세로
    for i in range(1, N):
        # cnt = 1
        cnt2 = 1
        for j in range(1, M):
            if rms[i-1][j-1] == rms[i-1][j] == 1:
                cnt += 1
            if rms[j-1][i-1] == rms[j][i-1] == 1:
                cnt2 += 1
    # print(cnt, cnt2)
    print(f'#{tc} {max(cnt, cnt2)}')

    ###################################################
    result = 0
    for i in range(1, N):
        cnt = 1
        cnt2 = 1
        for j in range(1, M):
            if rms[i-1][j-1] == rms[i-1][j] == 1:
                cnt += 1
                if result < cnt:
                    result = cnt
            if rms[j-1][i-1] == rms[j][i-1] == 1:
                cnt2 += 1
                if result < cnt2:
                    result = cnt2

    print(result)
    print(f'#{tc} {result}')