import sys
sys.stdin = open('input.txt')

N = int(input())
line = []
order = list(map(int, input().split()))

for i in range(1, N+1):
    line.insert(len(line)-order[i-1], i)

print(*line)
