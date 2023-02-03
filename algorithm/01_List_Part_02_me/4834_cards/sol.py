import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for i in range(T):
    card_num = int(input())
    card_num_list = list(map(int, input()))
    temp_list = [0] * 10
    for num in card_num_list:
        temp_list[num] += 1
        most_common = temp_list[0]
        most_idx = 0
        for idx in range(1, len(temp_list)):
            if most_common <= temp_list[idx]:
                most_common = temp_list[idx]
                most_idx = idx
    print(f'#{i+1} {most_idx} {most_common}')
