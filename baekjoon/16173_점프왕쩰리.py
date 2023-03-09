import sys
sys.stdin = open('input.txt')

dy = [1, 0]
dx = [0, 1]

def bfs(x, y):
    q = [(x, y)]
    while q:
        x, y = q.pop()
        move = map[x][y]
        for k in range(2):
            nx = x + dx[k] * move
            ny = y + dy[k] * move
            if 0 <= nx < N and 0 <= ny < N and map[nx][ny] == -1:
                return 'HaruHaru'
                break
            elif 0 <= nx < N and 0 <= ny < N and map[nx][ny] < N and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = 1
    return 'Hing'

N = int(input())
map = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
x, y = 0, 0
print(bfs(x, y))

