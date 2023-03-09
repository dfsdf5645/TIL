import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())

arr1 = []
arr2 = []
for i in range(N):
    x = input()
    arr1.append(x)
for i in range(M):
    y = input()
    arr2.append(y)

ans = list(set(arr1) & set(arr2))
ans.sort()
print(len(ans))
print(''.join(ans),end='')