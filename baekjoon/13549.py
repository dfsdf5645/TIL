import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt')

def bfs(start):
    q = [start]
    visited = [0] * (MAX+1)
    visited[start] = 1
    while q:
        start = q.pop(0)
        if start == K:
            print(visited[start] - 1)
            break
        for next in (start-1, start+1, start*2):
            if 0 <= next <= MAX and visited[next] == 0:
                if next == start*2:
                    visited[next] = visited[start]
                    q.insert(0, next) #순간이동이라 먼저탐색
                else:
                    q.append(next)
                    visited[next] = visited[start] + 1

MAX = 10 ** 5
N, K = map(int, input().split())

bfs(N)