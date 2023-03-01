N, M
A lst
B lst

result = 0
for i in range(M-N+1):
    tmp = 0
    for j in range(N):
        print(B[i+j] * A[j], end=' ')
    if result < tmp:
        result = tmp
    print(tmp)
print(result)

