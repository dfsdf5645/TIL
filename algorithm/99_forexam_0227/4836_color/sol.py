import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    arr = [[0] * 10 for _ in range(10)]
    N = int(input())
    for n in range(N):
        r1, c1, r2, c2, color = map(int, input().rstrip().split())
        if color == 1:
            for l in range(r1, r2+1):
                for m in range(c1, c2+1):
                    arr[l][m] += 1
        else:
            for l in range(r1, r2+1):
                for m in range(c1, c2+1):
                    arr[l][m] += 1

    count = 0
    for a in range(10):
        count += arr[a].count(2)

    print(f'#{tc} {count}')

#learn 2일차