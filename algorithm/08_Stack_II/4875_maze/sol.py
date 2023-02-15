#2가 어딘지 위치 먼저 찾기
#거기서 시작
#델타 탐색 상하좌우 인덱스 조사, 거기 갈수잇나 유망군 검색
#갈수있다면, 현재위치 위가 0이고 이전번 방문안햇으면 가기
#다음할일목록에 스택에?넣기
#반복문으로 상하좌우 다 조사 후 스택에 넣기 or 스택 넣자마자 이동
#반복문while해보고 재귀로 바꿔보기...

import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]  #split 없어야...
    print(maze)

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                x = i
                y = j

















