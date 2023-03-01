import sys
sys.stdin = open('input.txt')

###############함수로 풀기#######################
def delta(x, y):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    cnt = 0
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < N:
            cnt += abs(arr[nx][ny] - arr[i][j])
    return cnt

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        for j in range(N):
            ans += delta(i, j)
    print(ans)

####################식 하나로 풀기############################
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    result = 0
    for i in range(N):
        for j in range(N):
            cnt = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < N and 0 <= ny < N:
                    cnt += abs(arr[nx][ny] - arr[i][j])
            result += cnt
    print(result)

