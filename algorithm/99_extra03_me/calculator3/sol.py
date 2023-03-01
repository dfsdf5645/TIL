import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    L = int(input())
    cal = input()
    stack = []  # 연산자들 담아둘 스택
    result = ''  # 후위표기식으로 바꾼 결괏값
    # 전체 식 순회
    for char in cal:
        # 연산자들이라면
        if char in '+-*/()':
            # 연산자들의 우선순위에 맞춰 값들을 스택에 넣는 과정
            if char == '(':
                stack.append(char)
            elif char in '*/':
                while stack and stack[-1] in '*/':
                    result += stack.pop()
                stack.append(char)
            elif char in '+-':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.pop()  # 여는 소괄호 빼줌
        else:
            result += char
    while stack:
        result += stack.pop()

    # 후위표기식 연산
    for char in result:
        if char not in '+-*/':
            stack.append(char)
        else:
            x = int(stack.pop())
            y = int(stack.pop())
            if char == '+':
                stack.append(y + x)
            if char == '-':
                stack.append(y - x)
            if char == '*':
                stack.append(y * x)
            if char == '/':
                stack.append(y / x)

    print(f'#{tc}', *stack)
