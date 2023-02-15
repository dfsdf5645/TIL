import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    cal = input()
    stack = []     #연산자들 담아둘 스택
    result = ''    #최종결괏값
    #전체 식 순회
    for char in cal:
        #연산자들이라면
        if char in '+-*/()':
            #연산자들의 우선순위에 맞춰 값들을 스택에 넣는 과정
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
                stack.pop() #여는 소괄호 빼줌
        else:
            result += char
    while stack:
        result += stack.pop()

    print(result)
    # print(stack)
