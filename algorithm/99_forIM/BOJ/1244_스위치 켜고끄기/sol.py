import sys
sys.stdin = open('input.txt')

N = int(input())
first = list(map(int, input().split()))
print(first)

#
S = int(input())
for _ in range(S):
    s, num = map(int, input().split())
    if s == 1:

