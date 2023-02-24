import sys
sys.stdin = open('input.txt')

def bfs(s):
    q = []
    v = [0]*101
    ans = s
    #초기데이터 삽입, v표시
    q.append(s)
    v[s]=1

    while q:
        c = q.pop(0)
        if v[ans] < v[c] or v[ans]==v[c] and ans<c:
            ans = c
        for n in graph[c]:
            if v[n] == 0:
                q.append(n)
                v[n] = v[c]+1
    return ans


for tc in range(1, 11):
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    visited = [0] * 101
    graph = [[] for _ in range(101)]

    for i in range(0, N, 2):
        s, e = arr[i], arr[i+1]
        graph[s].append(e)
        # graph[s] = e

    print(f'#{tc} {bfs(S)}')