import sys
sys.stdin = open('sample_input.txt')

# 한줄에서 한개씩, 전체합
def search(col, cnt):
    global result
    if cnt > result:    # 가지치기
        return
    if col == N:
        if cnt < result:
            result = cnt
    else:
        for row in range(N):
            if not visited[row]:
                visited[row] = 1
                search(col+1, cnt+arr[col][row])
                visited[row] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 10 * N * N # 10보다 작은 자연수 주어지니 ,,,
    visited = [0] * N   # 방문 햇니안햇니

    search(0, 0)
    print(f'#{tc} {result}')