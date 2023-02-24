import sys
sys.stdin = open('input.txt')

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def search(x, y):
    visited = [[0]*100 for _ in range(100)]
    q = [(x, y)]
    visited[x][y] = 1
    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #maze 조건 빼먹지말기
            if 0 <= nx < 100 and 0 <= ny < 100 and maze[nx][ny] != 1 and visited[nx][ny] == 0:
                if maze[nx][ny] == 3:
                    return 1
                q.append((nx, ny)) #append x, y 아님
                visited[nx][ny] = visited[x][y] + 1
    return 0



for _ in range(1, 11):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(100)]
    # print(maze)
    # x, y = 0, 0 #x,y 초기설정

    for i in range(100):
        for j in range(100):
            if maze[i][j] == 2:
                x, y = i, j

    print(f'#{tc} {search(x, y)}')
