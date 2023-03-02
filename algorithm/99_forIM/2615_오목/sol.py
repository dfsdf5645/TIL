import sys
input = sys.stdin.readline

dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

def bfs(x, y):
    color = ba[x][y] #바둑알 색
    for k in range(4):
        cnt = 1 #바둑알
        nx = x + dx[k]
        ny = y + dy[k]

        while 0 <= nx < 19 and 0 <= ny < 19 and ba[nx][ny] == color:
            cnt += 1

            if cnt == 5: #5번가면 오목인지 판정...
                pass #실패한 경우
                break

                #성공한 경우
                print(color)
                print(x, y)
        break


ba = [list(map(int, input().split())) for _ in range(19)]

for i in range(19):
    for j in range(19):
        if ba[i][j] != 0:
            bfs(i, j)


