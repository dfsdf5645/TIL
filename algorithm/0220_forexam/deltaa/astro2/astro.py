import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # print(N, M)
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    dx = [1,1,0,-1,-1,-1,0,1]
    dy = [0,1,1,1,0,-1,-1,-1]

    result = 0
    for i in range(N):
        for j in range(M):
            cnt = 0
            for k in range(8):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < N and 0 <= ny < M:
                    if arr[i][j] > arr[nx][ny]:
                        cnt += 1
            if cnt >= 4:
                result += 1
    print(f'#{tc} {result}')
