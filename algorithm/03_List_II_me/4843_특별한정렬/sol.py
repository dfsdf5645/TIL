import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    n_list = list(map(int, input().split()))
    ans_list = []

    n_list.sort()
    for i in range(5):
        ans_list.append(n_list.pop(-1))
        ans_list.append(n_list.pop(0))

    print(f'#{tc}',*ans_list) #list 안에 있는 숫자만 빼오기
