def BFS(now):
    queue = [now] #할일목록
    print(now, end=' ')
    #방문표시 먼저 진행
    visited[now] = 1 #할일목록 잇는동안 반복문 돌려야되니 하나 먼저 넣어줘야함

    while queue:
        now = queue.pop(0) #젤처음 1은 이미 pop해서 삭제됏음
        for next in G[now]: #간선정보 잇는애들만!! 갈수잇는애들만 갖고 조사
            #해당 V의 인접정점W이면서, 여기 아직 방문안햇음
            if visited[next] == 0: #애초에 갈수잇는애들만 다 담아놧음, 갈수잇나 판단 불필요
                #방문한적잇는지만 판단하면됨
                #인접애들 queue에 추가
                queue.append(next)
                visited[next] = 1 #이미 할일목록에 잇으니 방문햇다고..중복체크되지않게
                print(next, end=' ')

V, E = map(int, input().split())

#간선정보 초기화
temp = list(map(int, input().split()))
print(temp)

#그래프 초기화
G = {key: 0 for key in range(V+1)}
print(G)

#인접행렬 작성
for i in range(E):
    n1, n2 = temp[i*2], temp[i*2+1]
    G[n1].append(n2)
    G[n2].append(n1)
print(G)

visited = [0 for _ in range(V+1)] #미로문제같은 (1,1)갔엇나 체크해야되면 방문표시도 이차원으로해야함
# BFS(1)