import sys
sys.stdin = open('input.txt')

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
            if 0 <= nx < N and 0 <= ny < M and trash[nx][ny] == 1:
                cnt += 1
                q.append((nx,ny))
                trash[nx][ny] = 2
    return cnt

N, M, K = map(int, input().split())
trash = [[0]*M for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split())
    trash[r-1][c-1] = 1

max_ans = 0
for i in range(N):
    for j in range(M):
        if trash[i][j] == 1:
            ans = bfs(i, j)
            if max_ans < ans:
                max_ans = ans
            result = max(max_ans, ans)
print(result)
