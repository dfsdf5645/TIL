import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    # 거꾸로 올라가 x좌표를 도출하는 방식
    for n in range(100):    #일단 지정된 도착점의 x좌표를 구하는 for문
        if arr[99][n] == 2: #마지막줄 x좌표 다 돌면서 2인곳 발견하면
            x = n           #그곳이 사다리도착점이자 우리가 거꾸로 출발할 x좌표

    y = 99 #젤 밑에줄에서부터 시작할거니까 y초기값 99 -> 계속 위로 올라가다 0이될때까지 반복
    #swea에 있는 바둑판 그림 보면서 읽어야 이해됨
    while True:
        #오른쪽이 1이어서 오른쪽으로 이동하는 경우
        if x < 99 and arr[y][x+1] == 1:         #x가 99 넘지않는선에서 오른쪽이 1이다?
            while x < 99 and arr[y][x+1] == 1:  #오른쪽이 계속 1인동안
                x += 1                          #오른쪽으로 이동이동
            else:                               #그러다 오른쪽에 더이상 1이 아니고 0이 나왔어
                y -= 1                          #그럼 멈추고 위로 한칸 올라가

        #왼쪽이 1이어서 왼쪽으로 이동하는 경우
        elif x > 0 and arr[y][x-1] == 1:        #x>=0이면 바둑판 넘어감 왼쪽이 1이다?
            while x > 0 and arr[y][x-1] == 1:   #왼쪽 계속 1인동안
                x -= 1                          #왼쪽으로 이동이동
            else:                               #그러다 왼쪽에 더이상 1이 아니고 0이면
                y -= 1                          #멈춰 그리고 위로 한칸 올라가

        #양쪽 다 0이라서 위로만 이동하는 경우
        else:
            y -= 1

        #계속 반복하다가 y=0이 되면 사다리출발점에 도달한거니까 break
        if y == 0:
            break
    print(f'#{tc} {x}') #그때의 x좌표를 출력함