A = int(input())


numbers = list(map(int, input().split()))

for i in range(A):
    max_h = len(numbers) - (i+1)

    for j in range(i+1, len(numbers)):
        if numbers[i] <= numbers[j]:
            max_h -= 1

    if result < max_h:
        result = max_h

print(f'#{tc} {result}')