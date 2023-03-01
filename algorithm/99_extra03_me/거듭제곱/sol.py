import sys
sys.stdin = open('input.txt')

for _ in range(1, 11):
    tc = int(input())
    N, M = map(int, input().split())

    # print(f'#{tc} {N**M}')

    # rlt = 1
    # for _ in range(M):
    #     rlt *= N
    # print(rlt)

    def power(a, n):
        if n == 1:
            return a

        return power(a, n - 1) * a

    print(f'#{tc} {power(N, M)}')