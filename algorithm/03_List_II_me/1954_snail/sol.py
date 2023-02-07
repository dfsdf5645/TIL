import sys
sys.stdin = open('input.txt')

#세울오빠
TC = int(input())
for T in range(1, TC + 1):
    N = int(input())

    if N == 1:  # N = 1 일 경우 그냥 1 을 출력
        print(f"#{T}")
        print(1)

    else:  # 아닐 경우
        new_mat = [[0] * N for j in range(N)]  # 먼저 출력할 행렬을 만들고
        new_list = list(range(1, N * N + 1))  # 들어갈 리스트들을 생성한다
        x = 0
        y = 0
        new_mat[0][0] = new_list[0]  # 행렬의 맨 왼쪽 위는 리스트의 첫번째 수를 저장하고 시작한다
        t = 1
        while new_mat[x][y + 1] == 0:  # 오른쪽, 아래, 왼쪽, 위 작업이 끝나고 다시 오른쪽 작업이 없을 경우 종료

            # 이 경우는 오른쪽으로 계속 가다가 더 이상 갈 곳이 없으면 종료
            while not new_mat[x][y + 1]:
                y = y + 1
                new_mat[x][y] = new_list[t]  # 리스트에서 t 번째 리스트를 저장ㄴ
                t = t + 1
                if y + 1 < N:
                    pass
                else:
                    break

            # 이 경우는 아래로 가다가 더 이상 갈 곳이 없으면 종료
            while not new_mat[x + 1][y]:
                x = x + 1
                new_mat[x][y] = new_list[t]
                t = t + 1
                if x + 1 < N:
                    pass
                else:
                    break

            # 이 경우는 왼쪽으로 가다가 더 이상 갈 곳이 없으면 종료
            while not new_mat[x][y - 1]:
                y = y - 1
                new_mat[x][y] = new_list[t]
                t = t + 1
                if y - 1 >= 0:
                    pass
                else:
                    break
            # 이경우는 위로 가다가 더 이상 갈 곳이 없으면 종료

            while not new_mat[x - 1][y]:
                x = x - 1
                new_mat[x][y] = new_list[t]
                t = t + 1
                if x - 1 >= 0:
                    pass
                else:
                    break
        # 그리고 결과 값을 종료
        print(f"#{T}")
        for i in new_mat:
            print(*i)
##############################################################성현님
def make_graph(n):
    # 번호를 저장해서 반환할 배열
    graph = [[0] * n for _ in range(n)]

    # 시작 위치
    x, y = 0, -1

    # 함수 내에서 사용할 방향
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    dir = 0

    for i in range(n ** 2 - 1, 0, -1):
        nx = x + dx[dir]
        ny = y + dy[dir]

        # 벽을 만나거나 값이 채워진 위치에서 방향 전환
        if nx < 0 or nx >= n or ny < 0 or ny >= n or graph[nx][ny] != 0:
            dir = (dir + 1) % 4

            nx = x + dx[dir]
            ny = y + dy[dir]

        graph[nx][ny] = i
        x, y = nx, ny

    return graph

arr = make_graph(5)

for i in arr:
    print(i)