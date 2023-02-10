import sys
sys.stdin = open('input.txt')


def check(arr):
    return 0 if check_list - arr else 1

T = int(input())

for tc in range(1, T+1):
    puzzle = [list(map(int, input().split())) for _ in range(9)]
    check_list = set(range(1, 10))  # 차집합을 구해 공집합이 되는지 비교하기 위한 베이스
    result = 1
    for i in range(9):
        row = set(puzzle[i])    # 각 행별 조사
        if not check(row):      # 공집합이 아니라면
            result = 0          # 중복되는 수가 있으므로 0
            break               # 조사 종료

        col = set()             # 각 열별 조사를 위한 set 구성
        for j in range(9):
            col.add(puzzle[j][i])   # 열별 값 추가
        if not check(col):      # 공집합이 아니라면
            result = 0          # 이하동문
            break

    for i in range(0, 9, 3):        # 3단계씩 건너 뛰며 조사
        for j in range(0, 9, 3):
            matrix = set()          # 3x3 배열에 대한 조사
            for x in range(3):      # i와 j가 3단계씩 건너 뛰므로 i+0, i+1, i+2를 조사하기 위해
                for y in range(3):
                    # i j => 0 0
                    # i+x j+y => 0+0 0+0 | 0+0 0+1 | ... | 0+2 0+0 | 0+2 0+2
                    # x와 y의 모든 상황 조사 후, i,j는 3스텝 건너뜀
                    # i j => 3 3
                    # i+x j+y => 3+0 3+0 | 3+0 3+1 | ... | 3+2 3+0 | 3+2 3+2
                    matrix.add(puzzle[i+x][j+y])
            if not check(matrix):   # 3x3 배열의 각 값으로 차집합 계산
                result = 0
                break
    print(f'#{tc} {result}')

