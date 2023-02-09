import sys
sys.stdin = open('pattern_input.txt', encoding = 'utf-8')

for _ in range(10):
    tc = int(input())
    pattern = input()
    target = input()
    count = 0
    for t_idx in range(len(target) - len(pattern)+1):
        for p_idx in range(len(pattern)):
            if pattern[p_idx] != target[t_idx + p_idx]:
                break
        else:
            count += 1


    print(count, target.count(pattern))