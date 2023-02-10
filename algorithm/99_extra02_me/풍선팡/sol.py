import sys
sys.stdin = open('input.txt')

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    paper = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0

    for i in range(N):
        for j in range(M):
            cnt = paper[i][j]
            for k in range(4):
                if 0 <= i+dy[k] <= N-1 and 0 <= j+dx[k] <= M-1:
                    cnt += paper[i+dy[k]][j+dx[k]]
            if max_cnt < cnt:
                max_cnt = cnt
    print(f'#{tc} {max_cnt}')