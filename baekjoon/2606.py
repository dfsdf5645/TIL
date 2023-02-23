import sys
sys.stdin = open('input.txt')

def virus(start):
    visited = [0] * (V+1)
    q = [start]
    visited[start] = 1
    cnt = 0
    while q:
        start = q.pop(0)
        cnt += 1
        for next in range(1,V+1):
            if G[start][next] == 1 and visited[next] == 0:
                q.append(next)
                visited[next] = visited[start] + 1
    return cnt - 1

V = int(input())
E = int(input())

G = [[0]*(V+1) for _ in range(V+1)]

for _ in range(E):
    x, y = map(int, input().split())
    G[x][y] = 1
    G[y][x] = 1

S = 1
print(virus(S))
