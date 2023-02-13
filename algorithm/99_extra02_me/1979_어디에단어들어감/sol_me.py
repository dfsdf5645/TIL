import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    paper = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for i in range(N):
        for j in range(N-K+1):
            if paper[i][j:j+K] == list(amp(int, '1'*K)):
                if j+K+1 >= N:
                    if paper[i][j-1] != 1:
                        cnt += 1
                else:
                    if paper[i][j-1] != 1 and paper[i][j+K+1] != 1:
                        cnt += 1

    for i in range(N):
        for j in range(N):
            paper[i][j] = paper[j][i]

    # for i in range(N):
    #     cnt2 = 0
    #     for j in range(N-K+1):
    #         if paper[i][j:j+K] == list(map(int, '1'*K)):
    #             cnt2 += 1
    # print(cnt+cnt2)
    print(cnt)


#백준 누울자리문제
#오늘 받아적은 답
#회문
#1)전치행렬해서 슬라이싱하기
#2)문자열더하기로 한번에 끝내기기