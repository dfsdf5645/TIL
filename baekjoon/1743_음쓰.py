import sys
sys.stdin = open('1743_음식물 피하기/input.txt')

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def bfs(x, y):
    q = [(x, y)]
    trash[x][y] = 2
    cnt = 1
    while q:
        x, y = q.pop(0)
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 < nx <= N and 0 < ny <= M and trash[nx][ny] == 1:
                q.append((nx, ny))
                trash[nx][ny] = 2
                cnt += 1
    return cnt

N, M, K = map(int, input().split())
trash = [[0]*(M+1) for _ in range(N+1)]
max_cnt = 0

for _ in range(K):
    r, c = map(int, input().split())
    trash[r][c] = 1

for i in range(1, N+1):
    for j in range(1, M+1):
        if trash[i][j] == 1:
            ans = bfs(i, j)
            if max_cnt < ans:
                max_cnt = ans
            result = max(ans, max_cnt)

print(result)