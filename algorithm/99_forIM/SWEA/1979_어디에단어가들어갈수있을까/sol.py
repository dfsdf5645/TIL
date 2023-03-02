import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    pz = [list(map(int, input().split())) for _ in range(N)]
    print(pz)

