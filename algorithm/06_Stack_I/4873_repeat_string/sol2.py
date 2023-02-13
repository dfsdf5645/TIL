import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    word = input()
    stack = []

    for char in word:
        if not stack:   #스택안에 값이 없으면
            stack.append(char)  #걍 추가
        elif stack and stack[-1] != char:
            stack.append(char)
        elif stack and stack[-1] == char: #뺄수있는상황
            stack.pop()

        #########반대로 적어보면###########
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    print(len(stack))