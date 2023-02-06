import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    #숫자리스트는 1-12
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    N = len(arr)
    J, K = map(int, input().split())

    ans_lst = [] #조건 해당하는 정답만 넣을 리스트
    for i in range(1, 1 << N):  # N = len(10개의 정수)
        # i -> N으로 만들 수 있는 모든 경우의 수
        # 1번째부터 2**n번째의 경우의 수
        a_list = [] #인덱스 일치하는... 애들만 넣을 리스트
        for j in range(12):  # 모든요소의 개수
            if i & (1 << j):  #i의 j번째 비트가 1인지아닌지 검사
                a_list.append(arr[j])
        if len(a_list) == J and sum(a_list) == K:
            ans_lst.append(a_list)
    ans = len(ans_lst)

    print(f'#{tc} {ans}')
