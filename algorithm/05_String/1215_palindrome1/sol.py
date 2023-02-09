import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    M = int(input())
    words = [list(map(str, input())) for _ in range(8)]

    cnt = 0
    for i in range(8):
        for j in range(9-M):
            org1 = ''
            org2 = ''
            for m in range(M):
                org1 += words[i][j+m]
                org2 += words[j+m][i]
            if org1 == org1[::-1]:
                cnt += 1
            if org2 == org2[::-1]:
                cnt += 1
    print(f'#{tc} {cnt}')

