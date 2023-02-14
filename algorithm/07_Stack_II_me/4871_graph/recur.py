import sys
sys.stdin = open('sample_input.txt')
#재귀로 하면 리턴값 운좋아야 나옴
def DFS(start):
    visited[start] = 1
    if start == G:
        return 1
    for next in range(1,V+1):
        if data[start][next] and not visited[next]:
            return DFS(next)

T = int(input())

for tc in range(1, T+1):
    V, E = map(int,input().split())

    #인접헹렬
    data = [[0]*(V+1) for _ in range(V+1)]
    #방문표시용 리스트
    visited = [0] * (V+1)

    #간선정보
    for i in range(E):
        x, y = map(int, input().split())
        print(x, y)
        data[x][y] = 1
        #data[y][x] = 1 하면 양방향

    #시작지점 S, 도칙지점 G
    S, G = map(int, input().split())

    print(DFS(S))
