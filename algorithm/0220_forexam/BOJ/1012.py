import sys
sys.setrecursionlimit(10**6)

for test_case in range(int(input())):
    M, N, E = map(int, input().split())
    node = [[0]*M for _ in range(N)]
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    cnt = 0
    for _ in range(E):
        x, y = map(int, input().split())
        node[y][x] = 1

    def dfs(y, x):
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if N > ny >= 0 and M > nx >= 0:
                if node[ny][nx] == 1:
                    node[ny][nx] = 0
                    dfs(ny, nx)

    for y in range(N):
        for x in range(M):
            if node[y][x] == 1:
                dfs(y, x)
                cnt += 1
    print(cnt)

# def bug(start):
#     visited[start] = 1
#     stack = [start]
#     cnt = 0
#     while stack:
#         stack.pop()
#         if start == G:
#             cnt += 1
#         for next in range(N*M):
#             if arr[start][next] and not visited[next]:
#                 visited[next] = 1
#                 stack.append(next)
#     return 0
#
# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]
#
# T = int(input())
# for tc in range(T):
#     M, N, K = map(int, input().split())
#     arr = [[0] * M for _ in range(N)]
#     # print(arr)
#     visited = [0] * 2500
#     stack = []
#     for _ in range(K):
#         x, y = map(int, input().split())
#         stack.append((x, y))
#         # arr[x][y] = 1
#     # print(stack)
#     # print(stack[-1][0])
#     # print(stack[-1][1])
#
#     # print(arr)
#     # for i in range(N):
#     #     for j in range(M):
#     #         for k in range(4):
#     #             i = stack[-1][0]
#     #             j = stack[-1][1]
#     #
#     #             nx = i + dx[k]
#     #             ny = j + dy[k]
#     #
#     #             if 0 <= nx < N and 0 <= ny < M:
#     #                 while arr[nx][ny] == 1:
#     #                     stack.pop((nx, ny))
#     #                 cnt += 1
#     #                 nx = stack[-1][0]
#     #                 ny = stack[-1][1]
#     for k in range(4):
#         x = stack[-1][0]
#         y = stack[-1][1]
#         # print(x, y)
#         nx = x + dx[k]
#         ny = y + dy[k]
#         if 0 <= nx < N and 0 <= ny < M:
#             while arr[nx][ny] == 1:
#                 if ((nx, ny)) in stack:
#                     stack.pop((nx, ny))
#             cnt += 1
#             nx = stack[-1][0]
#             ny = stack[-1][1]
#
#         print(stack)
#

