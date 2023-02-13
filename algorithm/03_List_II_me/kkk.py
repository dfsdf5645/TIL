T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_fn = 0
    for fi in range(N-M+1):
        for fj in range(N-M+1):
            fn = 0
            for i in range(M):
                for j in range(M):
                    fn += arr[fi+i][fj+j]
            
            if max_fn < fn:
                max_fn = fn

    print(f'#{tc} {max_fn}')