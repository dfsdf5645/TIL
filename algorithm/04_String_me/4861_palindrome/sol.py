import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    #글자 한글자씩 넣는거
    words = [list(map(str, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N-M+1):
            org1 = ''
            org2 = ''
            for m in range(M):
                org1 += words[i][j+m]
                org2 += words[j+m][i]
            if org1 == org1[::-1]:
                ans = org1
            elif org2 == org2[::-1]:
                ans = org2
    print(f'#{tc} {ans}')