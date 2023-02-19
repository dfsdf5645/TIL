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
        if char == '(' or char == '{':  # 왼쪽괄호면 일단 스택에 넣어
            stack.append(char)
        else:   # 왼쪽괄호가 아닌 다른 문자들에 대해
            if char == ')': # 오른쪽괄호면
                if stack and stack[-1] == '(': #스택에 값이 있고, 마지막이 여는 소괄호엿음
                    stack.pop()
                elif not stack: #()들은 다 삭제됐고 스택에 (가 더이상 없는데 )를 만난경우
                    result = 0
                    break
                elif stack[-1] != '(':  #스택에 {가 있는데 )를 만난경우
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

