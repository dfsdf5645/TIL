import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for i in range(T): # 전체 테스트케이스 개수 3개
    N, M = map(int, input().split()) # 10, 3 // 10개의 숫자를 3개씩 묶은값을 비교
    arr = list(map(int, input().split())) # [1,2,3,4,5,6,7,8,9,10]
    sum_list = [] # 3개씩 더한 값들을 넣을 빈 리스트 생성
    # arr에서 3개씩 더해주기 위한 for문
    # j는 3개 중 첫번째 인덱스
    for j in range(N-M+1): # 3개씩 묶어야되는데 마지막 3개는 [8,9,10]이고 시작인덱스가 8을 넘어가면안됨
        sum_num = 0 # 더한값 초기화
        for k in arr[j : j+M]: # arr[0:3], arr[1:4], arr[2:5] ... =>range(j, j+M)
            sum_num += k # 3개씩 더한거 추가 1+2+3, 2+3+4, ... 8+9+10 =>arr[j]
        sum_list.append(sum_num) # 리스트에 추가 sum_list = [6, 9, 12, 15, ... , 27]

    max_nums = sum_list[0] # 일단 젤 첫번째값으로 초기설정
    min_nums = sum_list[0] # 여기서부턴 리스트 내 숫자들로 최대최소값 구하는것과 동일한 방식

    for x in range(1, N-M+1): # 이미 sum_list[0]은 초기값이니 비교할 필요x, [1]부터 비교
        if max_nums < sum_list[x]: # 비교 후 재설정하기
            max_nums = sum_list[x]
        if min_nums > sum_list[x]:
            min_nums = sum_list[x]
    result = max_nums - min_nums
    print(sum_list)
    print(f'#{i+1} {result}')

#파이썬 SW문제해결 기본 - LIST1 learn