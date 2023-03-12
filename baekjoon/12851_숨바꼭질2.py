from collections import deque
import sys
sys.stdin = open('input.txt')

def bfs(start):
    global result
    q = deque()
    q.append(start)
    visited[start] = 0
    while q:
        start = q.popleft()
        if start == K:
            result += 1
            continue
        for next in (start*2, start+1, start-1):
            if 0 <= next < 100001 and (visited[next] == visited[start] + 1 or visited[next] == -1):
                visited[next] = visited[start] + 1
                q.append(next)

N, K = map(int, input().split())
visited = [-1] * 100001
result = 0



bfs(N)

print(visited[K])
print(result)