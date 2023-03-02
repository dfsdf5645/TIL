import sys
sys.stdin = open('input.txt')

N = int(input())
nums = list(map(int, input().split()))
# print(nums)

cnt = 1
result = []
for i in range(1, N):
    if nums[i-1] <= nums[i]:
        cnt += 1
    else:
        result.append(cnt)
        cnt = 1
result.append(cnt)


cnt2 = 1
result2 = []
for j in range(1, N):
    if nums[j-1] >= nums[j]:
        cnt2 += 1
    else:
        result.append(cnt2)
        cnt2 = 1
result.append(cnt2)


print(max(result))
