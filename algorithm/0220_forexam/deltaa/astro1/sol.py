import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, K, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [1, 1, 0, -1, -1, -1, 0, 1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    cnt = 0 #카운트 위치!!!!!!!!! 안이 아님!!!!
    for i in range(1,N-1):
        for j in range(1,M-1):
            b = []
            for k in range(8):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < N and 0 <= ny < M:
                    b.append(arr[nx][ny])
            if max(b) - min(b) <= K and arr[i][j] >= min(b) and arr[i][j] - min(b) <= H:
                cnt += 1
    print(f'#{tc} {cnt}')
