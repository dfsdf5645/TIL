word = input()
stack = []
result = 1
for char in word:
    if char == '(':
        stack.append(char)
    elif char == ')':
        if stack:
            stack.pop()
        else:
            result = -1
            break

else:
    if stack:
        result = -1