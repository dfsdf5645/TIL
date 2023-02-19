import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    word = input()
    result = 1
    stack = []
    for char in word:
        if char in '({':
            stack.append(char)
        else:
            if char == ')':
                if not stack or stack[-1] != '(':
                    result = 0
                    break
                else:
                    stack.pop()
            elif char == '}':
                if not stack or stack[-1] != '{':
                    result = 0
                    break
                else:
                    stack.pop()
    else:
        if stack:
            result = 0

    print(result)