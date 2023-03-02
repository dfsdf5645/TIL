import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())

garo = [0,M]
sero = [0,N]
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    if a == 0: #가로로 자르면
        garo.append(b)
    elif a == 1: #세로로 자르면
        sero.append(b)

garo.sort()
sero.sort()
# print(garo)
# print(sero)

g = []
for idx in range(len(garo)-1): #012
    sub = garo[idx+1]-garo[idx]
    g.append(sub)
g.sort()

s = []
for idx in range(len(sero)-1):
    subb = sero[idx+1]-sero[idx]
    s.append(subb)
s.sort()

# print(g)
# print(s)
print(s[-1] * g[-1])

