import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cnts = [0] * 5001

    for i in range(N):
        S, E = map(int, input().split())
        for j in range(S, E+1):
            cnts[j] += 1

    P = int(input())
    lst = []
    for _ in range(P):
        p = int(input())
        lst.append(cnts[p])
        # lst = [cnts[p] for _ in range(P)]

    print(f'#{tc}', *lst)