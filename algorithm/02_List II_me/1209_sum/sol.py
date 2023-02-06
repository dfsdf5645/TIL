import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    sum_list = []

    for i in range(100):
        cnt = 0
        for j in range(100):
            cnt += arr[i][j]
        sum_list.append(cnt)

    for j in range(100):
        cnt2 = 0
        for i in range(100):
            cnt2 += arr[i][j]
        sum_list.append(cnt2)

    cnt3 = 0 #대각선 우하향 방향
    for k in range(100):
        cnt3 += arr[k][k]
    sum_list.append(cnt3) #안으로 넣어버리면 여러값이 들어가버림 필요한건 다더한 한개값

    cnt4 = 0 #대각선 좌하향 방향
    for m in range(0, 100):
        cnt4 += arr[m][99-m]
    sum_list.append(cnt4)

    ans = max(sum_list)
    print(f'#{T} {ans}')
#---------수빈님 이중for문 하나로 끝낸 코드--------------------
import sys
sys.stdin = open("input.txt")

for test_case in range(10): # 케이스 10개이므로 총 10번 반복
    T = int(input()) # 각 케이스 넘버
    num_list = [] # 각 줄에 있는 100개씩의 숫자를 담은 리스트를 담을 바깥 리스트 선언
# 바깥 리스트 안에 담길 내부 리스트 만들기
    for _ in range(100): # 100번 반복. 왜? -> 100줄이니까 1줄 당 1번
        num_list.append(list(map(int, input().split()))) # 한 줄에 있는 숫자를 빈칸으로 구분해서 리스트에 담기

    sum_list = [] # 가로합, 세로합, 대각선의 각 합을 담을 리스트 선언 -> 가로합들과 세로합들과 대각선 합 비교해서 가장 큰 값 구하기.
    sum_rightdown = 0  # 오른쪽 위 대각선 합 -> 1번째부터 100번째 줄에 걸쳐서 대각선이 나오므로 반복문 안에 넣으면 안 됨!!
    sum_leftdown = 0  # 왼쪽 아래 대각선 합 -> 이하 동문

    for i in range(100):     # 리스트를 순회할 이중 반복문
        sum_garo = 0  # 가로합을 저장할 변수 초기화
        sum_saero = 0  # 세로합들을 저장할 변수 초기화
        for j in range(100):
            sum_garo += num_list[i][j]  # 가로합 더해준다.
            sum_saero += num_list[j][i]  # 세로합 더해준다.
            if i == j:  # 만약 두개의 인덱스가 같다면(오른쪽아래 대각선합)
                sum_rightdown += num_list[i][j]
            if i + j == 99:  # 만약 두개의 인덱스 합이 99라면(왼쪽 아래 대각선합)
                sum_leftdown += num_list[i][j]
        sum_list.append(sum_garo)   # -> 한 바퀴 돌고 나온 한 줄의 가로 총 합을 sum list에 추가한다.
        sum_list.append(sum_saero)  # -> 한 바퀴 돌고 나온 한 줄의 세로 총 합을 sum list에 추가한다.

    sum_list.append(sum_rightdown)  # -> 100 칸 100 줄의 모든 숫자들을 다 순회하며
    sum_list.append(sum_leftdown)   # -> 대각선 조건에 해당하는 인덱스의 숫자들을 더한 sum_대각선 변수를 추가.


    highest = 0                     # sum_list에서 가장 큰 값 for 반복문으로 구해서 highest변수에 할당하기.
    for num in sum_list:
        if num > highest:
            highest = num

    print(f'#{T} {highest}')