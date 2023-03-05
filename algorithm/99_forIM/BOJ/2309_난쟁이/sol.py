import sys
import random
sys.stdin = open('input.txt')

key = [int(input()) for _ in range(9)]

while True:
    lst = random.sample(key, 7)
    if sum(lst) == 100:
        for i in sorted(lst):
            print(i)
        break

