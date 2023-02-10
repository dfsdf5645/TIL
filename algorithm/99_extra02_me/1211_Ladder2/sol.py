#패딩 0으로, 범위내 체크 ans-1
T = int(input())
for tc in range(1, T+1):
    arr = []
    mn = 100 * 100
    for sj in range(1, 101):
        si, cnt, dj = 0,0,0
        #[1]시작지점 찾기
        if arr[si][sj] != 1:
            continue
        ci, cj = si, sj
        while ci < 99:
            cnt += 1
            if dj == 0:
                if arr[ci][cj-1] == 1:  #좌측
                    dj -= 1
                    cj -= 1
                elif arr[ci][cj+1] == 1: #우측
                    dj = 1
                    cj += 1
                else:
                    ci += 1
            else:
                if arr[ci][cj+dj]==1: #진행방향 1이라면
                    cj+=dj
                else: #진행방향이 막힌경우 아래로
                    dj = 0
                    ci += 1
        if mn >= cnt:
            mn, ans = cnt, sj-1
    print(f'#{tc} {ans}')