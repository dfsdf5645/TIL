import sys
sys.stdin = open('input_cal.txt')

T = int(input())

for tc in range(1, T+1):
    cal = input()
    stack = []     #연산자들 담아둘 스택
    result = 0   #최종결괏값
    for char in cal:
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
    print(stack)    #둘 다
    result = stack.pop()
    print(result)   #가능