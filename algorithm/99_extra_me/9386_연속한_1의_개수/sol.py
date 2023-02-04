import sys
sys.stdin = open('input1.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    LL = []

    L = list(input())
    for l in L:
        LL.append(int(l)) #[0, 0, 1, 1, 0, 0, 1, 1, 1, 0]

    count = 1
    max_count = 1
    for idx in range(1, N):
        if LL[idx-1] == 1 and LL[idx] == 1:
            count += 1
            if max_count < count:
                max_count = count
        elif LL[idx-1] == 0:
            count = 1
        else:
            count = 1

    print(f'#{tc} {max_count}')