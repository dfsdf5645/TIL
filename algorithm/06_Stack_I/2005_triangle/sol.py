import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    a = []
    for i in range(1,N+1):
        a.append(list(map(int,'1'*i)))
    # print(a)

    a[2][1] = a[1][0] + a[1][1]
    print(a)
    # for i in range(N):
    #     for j in range(N-i,-1,-1):
    #         print(a[i][j])
    #         #a[2][1] = a[1][0] + a[1][1]
    for i in range(2,N-1):
        for j in range(1,N-1):
            a[i][j] = a[i-1][j-1] + a[i-1][j]
    print(a)

    # 2,1 = 1,0 + 1,1
    # 3,1 = 2,0 + 2,1
    # 3,2 = 2,1 + 2,2
