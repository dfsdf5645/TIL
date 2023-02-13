bracket = input()
stack = []
result = 1
for char in bracket:
    if char == '(':
        stack.append(char)
    else:
        if stack:
            stack.pop()
        else:
            result = -1
            break
else:
    if stack:
        # print(stack)
        result = -1
print(result)