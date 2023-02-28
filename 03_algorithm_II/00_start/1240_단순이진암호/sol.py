import sys
sys.stdin = open('input.txt')

asc = {
    '0001101' : 0,
    '0011001' : 1,
    '0010011' : 2,
    '0111101' : 3,
    '0100011' : 4,
    '0110001' : 5,
    '0101111' : 6,
    '0111011' : 7,
    '0110111' : 8,
    '0001011' : 9,
}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    def search():
        # 모든 세로 줄에 대해서
        for i in range(N):
            # 가로 줄에 대해서는 뒤에서 앞으로
            for j in range(M - 1, -1, -1):
                # 만약 대상이 0이라면 그냥 다음 연산으로 넘어가기
                if arr[i][j] == '0': continue

                temp = []
                for k in range(j - 56 + 1, j, 7):
                    temp.append(arr[i][k:k + 7])

                odd_numbers = (asc[temp[0]] + asc[temp[2]] + asc[temp[4]] + asc[temp[6]])
                even_numbers = (asc[temp[1]] + asc[temp[3]] + asc[temp[5]] + asc[temp[7]])

                if (odd_numbers * 3 + even_numbers) % 10 == 0:
                    return odd_numbers + even_numbers
                else:
                    return 0

    print(f'#{tc} {search()}')