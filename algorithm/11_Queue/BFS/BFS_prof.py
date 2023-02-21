def BFS(now):
    queue = [now] #할일목록
    print(now, end=' ')
    #방문표시 먼저 진행
    visited[now] = 1 #할일목록 잇는동안 반복문 돌려야되니 하나 먼저 넣어줘야함

    while queue:
        now = queue.pop(0) #젤처음 1은 이미 pop해서 삭제됏음
        for next in range(1, V+1): #괄호 한줄 전체 다 조사하겟다.. now =1 이니
            #해당 V의 인접정점W이면서, 여기 아직 방문안햇음
            if G[now][next] == 1 and visited[next] == 0:
                #인접애들 queue에 추가
                queue.append(next)
                visited[next] = 1 #이미 할일목록에 잇으니 방문햇다고..중복체크되지않게
                print(next, end=' ')

V, E = map(int, input().split())

#간선정보 초기화
temp = list(map(int, input().split()))

#그래프 초기화
G = [[0] * (V+1) for _ in range(V+1)] #0번은 안쓸거니..

#인접행렬 작성
for i in range(E):
    n1, n2 = temp[i*2], temp[i*2+1]
    G[n1][n2] = 1
    G[n2][n1] = 1

visited = [0 for _ in range(V+1)] #미로문제같은 (1,1)갔엇나 체크해야되면 방문표시도 이차원으로해야함
BFS(1)