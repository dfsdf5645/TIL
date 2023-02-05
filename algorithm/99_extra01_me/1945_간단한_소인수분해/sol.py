import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    int_list = [2, 3, 5, 7, 11]
    count = {num: 0 for num in int_list}
    while N != 1: #N이 1이되면 멈춤
        for num in int_list:
            if not N % num:
                N //= num
                count[num] += 1
                break
    result = ' '.join(map(str, count.values()))
    print(f'#{tc} {result}')
