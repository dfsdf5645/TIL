import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    dir = 0

    for i in range(N):
        for j in range(N):
            for k in range(1, N * N+1):
                nx = i + dx[dir]
                ny = j + dy[dir]
                while arr[i][j] == 0:
                    if nx < 0 or nx >= N or ny < 0 or ny >= N or arr[nx][ny] == 0:
                        dir = (dir+1) % 4
                        nx = i + dx[dir]
                        ny = j + dy[dir]
                    arr[nx][ny] = k
                    i, j = dx[dir], dy[dir]

    print(arr)

    # for i in range(N**2-1, 0, -1):
    #     nx = x + dx[dir]
    #     ny = y + dy[dir]
    #
    #     if nx < 0 or nx >= N or ny < 0 or ny >= N or arr[nx][ny] != 0:
    #         dir = (dir + 1) % 4
    #
    #         nx = x + dx[dir]
    #         ny = y + dy[dir]
    #
    #     arr[nx][ny] = i
    #     x, y = nx, ny

    # for i in arr:
    #     print(*i)