import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, input()))

    visited = [0]*10
    for char in ai:
        visited[char] += 1

    max_count = 0       # 최대 출현 횟수
    max_val = 0         # 가장 큰 수
    for i in range(10):
        # 최대 출현 횟수가 visited i번째보다 작거나 같다면
        # 작거나 같아야 하는 이유는 뭘까?
        if max_count <= visited[i]:
            max_count = visited[i]
            max_val = i

    print(f'#{tc} {max_val} {max_count}')