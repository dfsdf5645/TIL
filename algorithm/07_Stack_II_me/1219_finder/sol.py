import sys
sys.stdin = open('input.txt')

def DFS(start):
    visited[start] = 1 #첫위치는 무조건 갓다고 찍어줘야하니 1
    stack = [start]
    while stack:
        start = stack.pop() #제일 최근꺼 뽑아줌 다음조사대상 뽑아줌
        # print(start, end=' ')
        if start == G:  # 현재 조사 대상이 도착지점이면?
            # 그럼 더 조사하지말고 그만
            return 1
        for next in range(1, 100):
            if data[start][next] and not visited[next]:
                visited[next] = 1
                stack.append(next)
    return 0

for tc in range(1, 11):
    T, V = map(int, input().split())
    data = [[0]*100 for _ in range(100)]
    visited = [0] * 100

    nums = list(map(int, input().split()))
    for i in range(0,len(nums),2):
        x, y = nums[i], nums[i+1]
        data[x][y] = 1

    S = 0
    G = 99
    print(f'#{tc} {DFS(S)}')
