import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    #글자 한글자씩 넣는거 미친
    words = [list(map(str, input())) for _ in range(N)]
    print(words)

    for i in range(N):
        for j in range(N-M+1):
            for k in range(M):
                words[i][j+k]

