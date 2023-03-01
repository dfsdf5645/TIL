import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(arr)

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    max_cnt = 0
    for i in range(N):
        for j in range(M):
            cnt = arr[i][j]
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < N and 0 <= ny < M:
                    cnt += arr[nx][ny]
            if max_cnt < cnt:
                max_cnt = cnt
    print(f'#{tc} {max_cnt}')
