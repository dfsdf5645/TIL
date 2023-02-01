import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    max_num = arr[0] #min, max값을 밑 for문안으로 넣으면 값 제대로 안나옴
    min_num = arr[0] #매번 arr[0]값으로 초기화돼서 .........
    for num in arr:
        if max_num < num:
            max_num = num
        if min_num > num:
            min_num = num
        result = max_num - min_num
    print(f'#{i+1} {result}')