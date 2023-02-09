import sys
input = sys.stdin.readline

N, M = map(int, input().split())

check = [list(input().split()) for _ in range(N)]
print(check)

