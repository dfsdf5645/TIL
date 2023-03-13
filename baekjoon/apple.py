import sys
sys.stdin = open('input.txt')

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]
dir = 0

def move1(x, y):
    st_x = 0
    st_y = 0
    cnt2 = 0
    while True:
        if st_x == x and st_y == y:
            break
        if st_y == y:
            cnt2 += 1
            while True:
                if st_x == x:
                    break
                st_x += dx[0]
        else:
            st_y += 1
    return cnt2

def move2(x, y):
    global a, p
    st_x = a
    st_y = p
    if x > st_x:
        if x < st_x and y > st_y:
            cnt = 3
        elif x > st_x and y > st_y:
            cnt = 3
        elif x > st_x and y < st_y:
            cnt = 1
        elif x < st_x and y < st_y:
            cnt = 2
    elif x < st_x:
        if x < st_x and y > st_y:
            cnt = 1
        elif x > st_x and y > st_y:
            cnt = 2
        elif x > st_x and y < st_y:
            cnt = 3
        elif x < st_x and y < st_y:
            cnt = 3
    elif y < st_y:
        if x < st_x and y > st_y:
            cnt = 2
        elif x > st_x and y > st_y:
            cnt = 3
        elif x > st_x and y < st_y:
            cnt = 3
        elif x < st_x and y < st_y:
            cnt = 1
    elif y > st_y:
        if x < st_x and y > st_y:
            cnt = 3
        elif x > st_x and y > st_y:
            cnt = 1
        elif x > st_x and y < st_y:
            cnt = 2
        elif x < st_x and y < st_y:
            cnt = 3
    return cnt

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    apple = [list(map(int, input().split())) for _ in range(N)]
    print(apple)

    M = 0
    for i in range(N):
        for j in range(N):
            if apple[i][j] != 0:
                M += 1
    # print(M)

    for i in range(N):
        for j in range(N):
            if apple[i][j] == 1:
                print(move1(i, j))

    #돌면서 1~M까지 리스트에다 넣고 하나씩 빼기...ㅅㅂ
    ans2 = 0
    for k in range(2, M+1):
        for i in range(N):
            for j in range(N):
                if apple[i][j] == k-1:
                    st_x, st_y = i, j
        for t in range(N):
            for u in range(N):
                if apple[t][u] == k:
                    x, y = t, u
        if x > st_x:
            if x < st_x and y > st_y:
                cnt = 3
            elif x > st_x and y > st_y:
                cnt = 3
            elif x > st_x and y < st_y:
                cnt = 1
            elif x < st_x and y < st_y:
                cnt = 2
        elif x < st_x:
            if x < st_x and y > st_y:
                cnt = 1
            elif x > st_x and y > st_y:
                cnt = 2
            elif x > st_x and y < st_y:
                cnt = 3
            elif x < st_x and y < st_y:
                cnt = 3
        elif y < st_y:
            if x < st_x and y > st_y:
                cnt = 2
            elif x > st_x and y > st_y:
                cnt = 3
            elif x > st_x and y < st_y:
                cnt = 3
            elif x < st_x and y < st_y:
                cnt = 1
        elif y > st_y:
            if x < st_x and y > st_y:
                cnt = 3
            elif x > st_x and y > st_y:
                cnt = 1
            elif x > st_x and y < st_y:
                cnt = 2
            elif x < st_x and y < st_y:
                cnt = 3
        print(cnt)