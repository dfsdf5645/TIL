import sys
sys.stdin = open('sample_input.txt')

#cnt는 합, c는 열
def search(c, cnt):
    global result
    if cnt > result:
        return

    if c == N:
        if cnt < result:
            result = cnt

    else:
        for r in range(N):
            if not visited[r]:
                visited[r] = 1
                search(c+1, cnt+arr[c][r])
                visited[r] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(arr)

    result = 10 * N * N
    visited = [0] * N

    search(0, 0)
    print(result)
