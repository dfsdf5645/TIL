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
        else:   # )를 만나면
            if stack:   # (이 들어있으니까
                stack.pop() # 한쌍 고대로 삭제
            else:   # 스택에 (도 없어
                result = -1 # 그럼 짝없는 )만 덜렁 있으니 -1
                break
    else:   # 다 돌았는데
        if stack:   # 스택에 값 남아있으면
            print(stack)
            result = -1
    print(result)
