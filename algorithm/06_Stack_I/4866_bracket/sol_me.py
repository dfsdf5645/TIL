import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    word = input()
    result = 1
    stack = []
    for char in word:
        if char == '(' or '{':
            stack.append(char)
        else:
            if char == ')' or '}':
                stack.pop()
