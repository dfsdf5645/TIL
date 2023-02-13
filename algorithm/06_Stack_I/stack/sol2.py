#스택을 만든다
stack = []

#스택에 값을 추가한다
stack.append('A')
print(stack)

#스택에 값을 계속 추가한다
stack.append('A')
stack.append('B')
stack.append('C')
stack.append('D')
print(stack)

#스택에서 값 제거한다
print(stack.pop())
print(stack)

#스택의 가장 마지막 요소를 조회한다
print(stack[-1])

print(bool(len(stack))) #true면 값이 있는거
