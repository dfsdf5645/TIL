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
            if 0 <= nx < 16 and 0 <= ny < 16 and maze[nx][ny] != 1 and visited[nx][ny] == 0:
                if maze[nx][ny] == 3:
                    return 1
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
    return 0

for _ in range(1, 11):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    visited = [[0]*16 for i in range(16)]
    x, y = 0, 0

    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                x, y = i, j
    print(f'#{tc} {search(x, y)}')