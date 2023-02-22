import sys
sys.stdin = open('input.txt')

def bfs(start):
    q = [start]
    visited = [0] * (MAX+1) #안하고 임의숫자 넣으면 인덱스에러뜸
    visited[start] = 1
    while q:
        start = q.pop(0)
        if start == K:
            return visited[start] - 1
        for next in (start-1, start+1, start*2):
            if 0 <= next <= MAX and visited[next] == 0:
                q.append(next)
                visited[next] = visited[start] + 1


MAX = 10 ** 5
N, K = map(int, input().split())

print(bfs(N))