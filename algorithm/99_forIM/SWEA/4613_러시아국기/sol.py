import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    flag = [list(input()) for _ in range(N)]
    print(flag)

    #4줄짜리면
    #1줄 w /2줄 b / 3,4줄 r
    #1줄 w / 2,3줄 b / 4줄 r
    #1,2줄 w / 3줄 b / 4줄 r
    #모든 경우를 다 세는 거임 그냥

    for i in range(N - 2): #01
        pass
        for j in range(i + 1, N - 1):
            pass
            for k in range(j + 1, N):
                pass