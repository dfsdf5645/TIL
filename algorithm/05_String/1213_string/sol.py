import sys
sys.stdin = open('pattern_input.txt', encoding = 'utf-8')

pattern = input()
target = input()

p_idx = 0
t_idx = 0

count = 0

while t_idx < len(target):
    if target[t_idx] == pattern[p_idx]:
        p_idx += 1
        t_idx += 1
    if p_idx == len(pattern):
        count += 1 #패턴 한번 찾았음
        p_idx = 0 #다음위치부터는 처음부터 다시 조사
    if target[t_idx] != pattern[p_idx]:
        t_idx = t_idx - p_idx
        t_idx += 1
        p_idx = 0


    print(pattern, target)