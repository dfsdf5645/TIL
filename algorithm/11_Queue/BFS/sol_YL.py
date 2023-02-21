#연습문제3
#V는 정점 번호, E는 엣지개수
import sys
sys.stdin = open('input.txt')

def bfs(v, N):
    visited = [0] * (N+1)   # visited 생성
    q = [v]                 # 큐 생성
                            # 시작점 인큐 한번에
    visited[v] = 1          # 시작점 인큐 표시
    while q:                # q가 비어있지않으면
        t = q.pop(0)        # 디큐
        print(t, end=' ')   # t에서 처리할 일
        for v in adjL[t]:   # t에 인접이고 방문한 적 없는 v
            if visited[v] == 0: # v 변수 재활용 그냥 i 해도됨
                q.append(v) # v 인큐
                visited[v] = visited[t] + 1 # v 인큐되었음 표시 그 상위보다 1 더함
    print()
    print(visited)  # visited 정보도 표시

V, E = map(int, input().split())
arr = list(map(int, input().split()))
adjL = [[] for _ in range(V+1)]
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjL[n1].append(n2) #방향표시 없으니 양쪽 다 해줘야함
    adjL[n2].append(n1)

bfs(1, V) #시작정점 1, V 마지막 정점