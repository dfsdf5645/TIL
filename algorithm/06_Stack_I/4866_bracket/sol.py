import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    word = input()
    # print(word)

    #최종 결괏값
    result = 1
    stack = []
    for char in word:
        if char == '(' or char == '{':
            stack.append(char)
        else:
            if char == ')':
                if stack and stack[-1] == '(': #스택에 값이 있고, 마지막이 여는 소괄호엿음
                    stack.pop()
                elif not stack: #스택이 비었는데
                    result = 0
                    #한번이라도 실패 시 더 이상 조사할필요 없다
                    break
                elif stack[-1] != '(':
                    result = 0
                    break
            if char == '}':
                if not stack or stack[-1] != '{':
                    result = 0
                    break
                else:
                    stack.pop()
    if stack:
        result = 0 #조사 다 끝났는데 스택 남은 경우

    print(result)

