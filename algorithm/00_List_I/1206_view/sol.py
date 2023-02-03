import sys

sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))

    result = 0
    # 양 끝 2자리 무시
    for i in range(2, N-2):
        # 현재 조사대상의 높이 : 최대 조망권
        tmp = arr[i]
        # 현재 위치를 기준으로 좌우 2칸씩 조사
        for j in range(i-2, i+3):
            # 나랑 나를 비교할 필요 없음
            if i == j:
                continue
            # 조사 대상이 양 옆보다 크고,
            # 그 둘의 차이가 최대 조망권보다 작으면
            if arr[i] > arr[j] and tmp > arr[i] - arr[j]:
                # 최대 조망권을 변경
                tmp = arr[i] - arr[j]
            # 만약 조사 대상의 양옆이 나와 크거나 같은 경우가 한번이라도 있으면
            # 더 이상 조사할 필요 없음
            elif arr[i] <= arr[j]:
                break
        # break문으로 종료되지 않았다면 (더 이상 조사할 필요가 없는 경우가 없었다면)
        # 정상적으로 모두 조사한 것이므로
        else:
            # i번쨰 위치 건물의 조망권 크기 더하기
            result += tmp
    print(f'#{tc} {result}')
