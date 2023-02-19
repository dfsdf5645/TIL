import sys
sys.stdin = open('input.txt')

def finder(start):
    visited[start] = 1
    if start == 99:
        return
    for k in range(1, 100):
        if G[start][k] == 1 and visited[k] == 0:
            finder(k)

for i in range(1, 11):
    tc, l = map(int, input().split())
    stack = list(map(int, input().split()))

    G = [[0]*100 for _ in range(100)]
    visited = [0] * 100
    for i in range(l):
        G[stack[i*2]][stack[i*2+1]] = 1

    finder(0)
    print(visited[99])
