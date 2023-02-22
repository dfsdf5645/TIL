import sys
sys.stdin = open('input.txt')

#일자로 숫자 주어짐
'''
V, E = map(int, input().split())
arr = list(map(int, input().split())
adj = [[0]*(V+1) for _ in range(V+1)]
adjv = [[] for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj[v1][v2] = 1
    adj[v2][v1] = 1
    
    adjv[v1].append(v2)
    adjv[v2].append(v1)
'''
#대박적..ㅋㅎ 리스트명 대충 G로 지어서 오류뜸
def dfs(start):
    visited = [0] * 100
    stack = [start]
    visited[start] = 1
    while stack:
        start = stack.pop(0)
        if start == G:
            return 1
        for next in range(1, 100):
            if data[start][next] and not visited[next]:
                stack.append(next)
                visited[next] = 1
    return 0

for _ in range(1, 11):
    tc, E = map(int, input().split())
    nums = list(map(int, input().split()))
    data = [[0]*100 for _ in range(100)]

    # print(arr)
    for i in range(E):
        x, y = nums[i*2], nums[i*2+1]
        data[x][y] = 1

    S = 0
    G = 99
    print(f'#{tc} {dfs(S)}')

# def DFS(start):
#     visited[start] = 1 #첫위치는 무조건 갓다고 찍어줘야하니 1
#     stack = [start]
#     while stack:
#         start = stack.pop() #제일 최근꺼 뽑아줌 다음조사대상 뽑아줌
#         # print(start, end=' ')
#         if start == G:  # 현재 조사 대상이 도착지점이면?
#             # 그럼 더 조사하지말고 그만
#             return 1
#         for next in range(1, 100):
#             if data[start][next] and not visited[next]:
#                 visited[next] = 1
#                 stack.append(next)
#     return 0
#
# for tc in range(1, 11):
#     T, V = map(int, input().split())
#     data = [[0]*100 for _ in range(100)]
#     visited = [0] * 100
#
#     nums = list(map(int, input().split()))
#     for i in range(0,len(nums),2):
#         x, y = nums[i], nums[i+1]
#         data[x][y] = 1
#
#     S = 0
#     G = 99
#     print(f'#{tc} {DFS(S)}')
