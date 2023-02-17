import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [[0 for _ in range(10)] for _ in range(10)]
    result = 0
    for _ in range(N):
        r1, c1, r2, c2, c = map(int, input().split())
        for x in range(r1, r2+1):
            for y in range(c1, c2+1):
                matrix[x][y] += c
                if matrix[x][y] == 3:

                    result += 1

    print(f'#{tc} {result}')