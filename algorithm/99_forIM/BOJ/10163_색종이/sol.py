import sys
sys.stdin = open('input.txt')

paper = [[0]*1001 for _ in range(1001)]
N = int(input())

for k in range(1,N+1):
    x, y, width, height = map(int, input().split())
    for i in range(x, x + width):
        for j in range(y, y + height):
            paper[i][j] = k

for l in range(1, N+1):
    cnt = 0
    for lst in paper:
        cnt += lst.count(l)
    print(cnt)
