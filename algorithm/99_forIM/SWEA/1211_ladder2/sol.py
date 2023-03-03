import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    # print(arr)

    start = []
    for i in range(100):
        if arr[0][i] == 1:
            start.append(i)
    print(start)
    # start = x
    y = 0

    ans = []
    for st in start:
        cnt = 0
        while True:
            if y == 99:
                ans.append((st, cnt))
                break
            if st > 0 and arr[y][st - 1] == 1:
                while st > 0 and arr[y][st - 1] == 1:
                    st -= 1
                else:
                    y -= 1
            elif st < 99 and arr[y][st + 1] == 1:
                while st < 99 and arr[y][st + 1] == 1:
                    st += 1
                else:
                    y -= 1
            else:
                y -= 1

        print(ans)
            # print(f'#{tc} {st}')