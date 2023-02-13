import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    bracket = input()
    stack = []
    result = 1
    for char in bracket:
        if char == '(':
            stack.append(char)  #여는 소괄호만 넣어줌
            # print(stack)
        else:
            if stack:
                stack.pop()
            else:
                result = -1
                break
    else:
        if stack:
            print(stack)
            result = -1
    print(result)
