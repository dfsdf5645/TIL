import sys
sys.stdin = open('s_input.txt')

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def search(x, y):
    global N
    stack = [(x, y)]
    cnt = 0
    while stack:
        x, y = stack.pop()
        cnt += 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if room[nx][ny] == room[x][y] + 1:
                    stack.append((nx, ny))
    return cnt

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    # print(room)

    max_cnt = 0
    for i in range(N):
        for j in range(N):
            cnt = search(i, j)
            if max_cnt < cnt:
                max_cnt = cnt
                ans1 = room[i][j]
                ans2 = cnt
            elif max_cnt == cnt:
                ans1 = min(room[i][j], ans1)
                ans2 = cnt
    print(f'#{tc} {ans1} {ans2}')