import sys
sys.stdin = open('input.txt')

N = int(input())
parent = [0] * (N+1)
left = [0] * (N+1)
right = [0] * (N+1)

for i in range(E):
    if left[p] == 0:  # 아직 왼쪽 자식 없으면
        left[p] = c  # p번의 왼쪽 자식 c
    else:  # 왼쪽에 자식 있으면
        right[p] = c  # 오른쪽에 자식정보 넣음
    parent[c] = p

for _ in range(N-1):
    p, c = map(int, input().split())
    if left[p] == 0:  # 아직 왼쪽 자식 없으면
        left[p] = c  # p번의 왼쪽 자식 c
    else:  # 왼쪽에 자식 있으면
        right[p] = c  # 오른쪽에 자식정보 넣음
    parent[c] = p
