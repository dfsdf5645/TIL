#부분집합 합 문제 구현하기
#10개의 정수를 입력받아 부분집합의 합이 0이 되는 것이 존재하는지를 계산하는 함수

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split())) #숫자리스트
    N = len(arr) #10개

    #원소 N개의 모든 경우의 수
    #2**N은 1<<N과 같다
    #원소의 개수가 3개라고 할 때,
    #2**3 = 8
    #1<<3 -> 이진수 1000 -> 8
    #0001 -> 1을 왼쪽으로 3번 밀면
    #1000
    print(1<<3)
    print(bin(1000))
    print(bin(125))
    result = 0
    for i in range(1, 1<<N): #N = len(10개의 정수)
        # i -> N으로 만들 수 있는 모든 경우의 수
        # 1번째부터 2**n번째의 경우의 수
        for j in range(N): #모든요소의 개수
            if i & (1<<j): #i의 j번째 비트가 1인지아닌지 검사
                print(arr[j])
                result += arr[j]
        if result == 0:
            print(1)
            break
    else:
        print(0)