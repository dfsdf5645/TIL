import sys
sys.stdin = open('input.txt')

for k in range(1, 11):
    flatten_try = int(input())
    height = list(map(int, input().split()))

    for i in range(flatten_try):
        idx_max = 0
        idx_min = 0
        result_max = height[0]
        for num in range(1, len(height)):
            if result_max < height[num]:
                result_max = height[num]
                idx_max = num
        height[idx_max] -= 1

        result_min = height[0]
        for num in range(1, len(height)):
            if result_min > height[num]:
                result_min = height[num]
                idx_min = num
        height[idx_min] += 1

    result_max_final = 0
    result_min_final = 100
    for n in height:
        if n > result_max_final:
            result_max_final = n
        if n < result_min_final:
            result_min_final = n
    ans = result_max_final - result_min_final
    print(f'#{k} {ans}')



# ###############################################
# #
# # import sys
# sys.stdin = open('input.txt')
#
# ## 그리드? 무식하게? 풀었다.
# ## list들을 계속 돌리면서 가장 큰 곳에서 가장 작은 곳으로 하나씩 넘겨주고 num을 하나씩 뺴줌
# for i in range(1, 11):
#     num = int(input())
#     ls = list(map(int,input().split()))
#     lenth = len(ls)
#
#     while num > 0:              # 횟수가 끝날때까지
#         M = 0                   # 최댓값을 넣을 M
#         Mj = 0                  # 최댓값의 위치 Mj
#         m = 100                 # 최솟값을 넣을 m
#         mj = 0                  # 최대값의 위치 mj
#         for j in range(lenth):
#             if ls[j] > M:       # 리스트 중에 최대값을 구함
#                 M = ls[j]
#                 Mj = j
#
#             if ls[j] < m:       # 리스트 중에 최소값을 구함
#                 m = ls[j]
#                 mj = j
#         if m == M:              # 만약 최대값과 최소값이 같은 경우 while문을 끝냄
#             break
#         else:                   # 아니면
#             ls[Mj] -= 1         # 최대값에 1을 빼주고
#             ls[mj] += 1         # 최소값에 1을 더해줌
#         num -= 1                # 횟수를 하나 빼줌
#     maxx = 0                    # 이제 작업이 끝나고 최대값과
#     mini = 100                  # 최소값을 구함
#     for j in ls:
#         if maxx < j:
#             maxx = j
#         if mini > j:
#             mini = j
#     print(f"#{i}",maxx- mini)   #최대값과 최소값의 차이를 구함
##############################################333
#
# flatten_try = int(input())
#
# height = list(map(int, input().split()))
#
# count = 0
# while count <= flatten_try:
#     result_max = height[0]
#     for num in range(len(height)):
#         if result_max < height[num]:
#             result_max = height[num]
#         height.append(height[num] -1)
#         height.remove(height[num])
#
#     result_min = height[0]
#     for num in range(len(height)):
#         if result_min > height[num]:
#             result_min = height[num]
#         result_min = height[num] + 1
#
#     count += 1
#
# print(result_max)
# print(result_min)
#
#
#
