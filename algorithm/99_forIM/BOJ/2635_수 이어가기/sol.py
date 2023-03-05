import sys
sys.stdin = open('input.txt')

N = int(input())
lst = []
max_len = []

for num in range(N+1):
    lst = [N, num]
    while True:
        sub = lst[-2] - lst[-1]
        if sub < 0:
            break
        lst.append(sub)
        if len(max_len) < len(lst):
            max_len = lst
print(len(max_len))
print(*max_len)