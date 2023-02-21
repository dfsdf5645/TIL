def bfs(G, v):  #그래프 G, 탐색 시작점 v
    visited = [0] * (n+1)   #n: 정점의 개수 1~n번
    queue = []              #큐 생성
    queue.append(v)         #시작점 v를 큐에 삽입 = enqueue()
    ######이까지가 초기에 해야하는#### 외우기
    while queue:            #큐가 비어있지 않은 경우
        t = queue.pop(0)    #큐의 첫번째 원소 반환 = dequeue()
        if not visited[t]:  #방문되지 않은 곳이라면
            visited[t] = True #방문했다 표시
            visit(t)        #정점 t에서 할 일 (문제마다 다름)
            for i in G[t]:  #t와 연결된 모든 정점에 대해
                if not visited[i]: #방문되지 않은 곳이라면
                    queue.append(i) #큐에 넣기 (담에 방문하게)

#노션 참고, 초기화 과정에 하나 더 추가
def bfs(G, v, n):  #그래프 G, 탐색 시작점 v
    #visited = [0] * (n+1)   #n: 정점의 개수 1~n번
    #queue = []              #큐 생성
    #queue.append(v)         #시작점 v를 큐에 삽입 = enqueue()
    visited[v] = 1          #시작점 '인큐'되었음을 표시 > 방문 대신
    ######이까지가 초기에 해야하는####
    # while queue:            #큐가 비어있지 않은 경우
    #     t = queue.pop(0)    #큐의 첫번째 원소 반환 = dequeue()
            #꺼내는 애들은 이미 visited에 없는거 확인됨!!
    #### 밑에 두 줄이 필요없음 ####
        if not visited[t]:  #방문되지 않은 곳이라면 >>> 이 과정이 필요없음
            visited[t] = True #방문했다 표시
    #### 방문여부 확인할 필요 없음 ####
            # visit(t)        #정점 t에서 할 일 (문제마다 다름)
            #미로의 경우, 내가 찾는 목적지인지 확인
            if t == G: return 1 다 돌때까지도 못찾으면 while문 빠져나와서 return 0해 등..
            # for i in G[t]:  #t와 연결된 모든 정점에 대해
            #     if not visited[i]: #방문되지 않은 곳이라면
            #        queue.append(i) #큐에 넣기 (담에 방문하게)
                    visited[i] = visited[n] + 1 #큐에 넣었다고 표시해줌,n으로부터 1만큼