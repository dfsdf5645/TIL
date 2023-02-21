import sys
sys.stdin = open('input.txt')

def bfs(start):
    visited = [0] * (V+1)
    q = [start]
    visited[start] = 1
    while q:
        start = q.pop(0)
        if start == G:
            return visited[start] - 1 #start를 안갓는데 1로 잡앗으니
        for next in range(1,V+1):
            if adjL[start][next] == 1 and visited[next] == 0:
                q.append(next)
                visited[next] = visited[start] + 1
    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split()) #간선의 양쪽 노드번호 주어짐

    adjL = [[0]*(V+1) for _ in range(V+1)]

    for i in range(E):
        x, y = map(int, input().split())
        adjL[x][y] = 1
        adjL[y][x] = 1

    S, G = map(int, input().split())  #출발노드S, 도착노드G

    print(f'#{tc} {bfs(S)}')
