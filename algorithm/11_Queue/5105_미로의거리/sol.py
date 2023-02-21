import sys
sys.stdin = open('input.txt')

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def search(x, y):
    q = [(x, y)]
    visited[x][y] = 1
    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and maze[nx][ny] != 1 and visited[nx][ny] == 0:
                if maze[nx][ny] == 3:
                    return visited[x][y] - 1
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for i in range(N)]
    x, y = 0, 0

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                x, y = i, j
    print(f'#{tc} {search(x, y)}')