import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, input()))

    visited = [0] * 10          # 각 수의 등장 횟수 체크
    max_count = 0               # 최대 출현 횟수
    max_val = 0                 # 가장 큰 수
    for i in ai:                # 원본 리스트를 순회
        visited[i] += 1         # 방문횟수 1 증가
        # 지금까지 가장 많았던 수보다, 방금 체크한 수가 더 많이 나왔다면
        if max_count < visited[i]:
            max_count = visited[i]
            max_val = i
        # 지금까지 수와 동일하고, 최댓값이 더 크다면
        elif max_count == visited[i] and max_val < i:
            max_count = visited[i]
            max_val = i

    print(f'#{tc} {max_val} {max_count}')


