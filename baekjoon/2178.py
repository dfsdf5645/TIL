import sys
sys.stdin = open('input.txt')

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def bfs(x, y):
    global N, M
    q = [(x, y)]
    visited[x][y] = 1
    while q:
        x, y = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and maze[nx][ny] != 1 and visited[nx][ny] == 0:
                if nx == (N-1) and ny == (M-1):
                    return visited[nx][ny]
                    break
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
    return visited[nx][ny]


N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
print(maze)

visited = [[0]*M for _ in range(N)]

x, y = 0, 0
print(bfs(x, y))