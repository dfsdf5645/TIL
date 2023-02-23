import sys
sys.stdin = open('input.txt')

def bfs(s):
    queue = [s]
    visited[s] = 0
    while queue:
        x = queue.pop(0)
        for i in graph[x]:
            if visited[i] == 0:
                visited[i] = visited[x] + 1
                queue.append(i)

for tc in range(1, 11):
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    visited = [0] * 101
    graph = [[] for _ in range(101)]

    for i in range(0, N, 2):
        graph[arr[i]].append(arr[i + 1])

    bfs(S)
    a = max(visited)
    max_n = 0
    for i in range(len(graph)):
        if visited[i] == a and max_n < i:
            max_n = i
    print(f'#{tc} {max_n}')