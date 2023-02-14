import sys
sys.stdin = open('sample_input.txt')

def DFS(start):
    #첫 시작위치 이아무튼 방문함
    visited[start] = 1
    stack = [start]
    while stack:
        start = stack.pop()
        print(start, end=' ')
        if start == G:  #현재 조사 대상이 도치ㅏㄱ지잠?
            #그럼 더 조사하지말고 ㄱ,만
            return 1
        for next in range(1, V+1):
            if data[start][next] and not visited[next]:
                visited[next] = 1
                stack.append(next)
    return 0


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
