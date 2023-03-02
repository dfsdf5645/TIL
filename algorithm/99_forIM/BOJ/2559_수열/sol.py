import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

summ = [0] * (N+1)
for i in range(N):
    summ[i+1] = summ[i] + arr[i]

ans = []
for j in range(N+1-K):
    ans.append(summ[j+K]-summ[j])

print(max(ans))

############################
# temp = list(map(int, input().split()))
# result = sum(temp[0:K])
# for i in range(1, N-K+1):
#     if temp[i+K-1] > temp[i-1]:
#         A = sum(temp[i:i+K])
#         if result < A:
#             result = A
#     else:
#         continue
# print(result)

# result = [0]
# for i in range(0, N-K+1):
#     a = sum(nums[i:i+K])
#     if result[0] < a:
#         del result[0]
#         result.append(a)
#
# print(*result)
# print(max(result))
