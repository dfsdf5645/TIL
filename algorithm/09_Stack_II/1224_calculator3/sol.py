import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    cal = input()
    stack = []
    result = ''
    for char in cal:
        if char == '+':
            while stack and stack[-1] in '+':
                result += stack.pop()
            stack.append(char)
        else:
            result += char
    while stack:
        result += stack.pop()

    for char in result:
        if char not in '+': #숫자면
            stack.append(char)  #빈 스택에 넣어줌
        else:
            x = int(stack.pop())
            y = int(stack.pop())
            if char == '+':
                stack.append(x + y)

    print(f'#{tc}', *stack)

