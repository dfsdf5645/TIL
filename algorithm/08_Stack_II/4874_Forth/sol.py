import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    cal = input().split()
    stack = []
    n_cnt = []  #숫자만 넣은 리스트
    p_cnt = []  #연산자랑 .만 넣은 리스트
    for char in cal:
        if char in '+-*/.':
            p_cnt.append(char)
        else:
            n_cnt.append(char)

    #정상이라면 저 두 리스트 개수가 같아야함
    #원래 숫자보다 연산자 개수가 한 개 적어야하니까
    #만약 개수가 다르다면 에러
    #개수가 같다면 밑에 저거 실행

    if len(n_cnt) != len(p_cnt):
        print(f'#{tc}', 'error')
    else:
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
                    stack.append(y // x)
        for i in stack:
            if i == '.':
                stack.remove(i)
        print(f'#{tc}', *stack)
