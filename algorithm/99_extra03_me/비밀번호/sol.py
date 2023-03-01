import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    L, N = input().split()
    stack = []
    for char in N:
        if not stack:
            stack.append(char)
        elif char == stack[-1]:
            stack.pop()
        else:
            stack.append(char)

    print(f'#{tc}', ''.join(stack))
