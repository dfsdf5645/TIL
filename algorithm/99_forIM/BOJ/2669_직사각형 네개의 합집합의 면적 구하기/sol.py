import sys
sys.stdin = open('input.txt')

paper = [[0]*100 for _ in range(100)]
# print(paper)


for _ in range(4):
    x, y, xx, yy = map(int, input().split())
    for i in range(x, xx):
        for j in range(y, yy):
            paper[i][j] = 1


cnt = 0
for lst in paper:
    cnt += lst.count(1)
print(cnt)

# print(paper)
