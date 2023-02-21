from collections import deque
import sys
sys.stdin = open('input.txt')

def untilzero(lst):
    while lst[-1] > 0:
        for i in range(1, 6):
            if lst[0] - i > 0:
                lst.append(lst[0] - i)
                lst.pop(0)
            else:
                lst.append(0)
                lst.pop(0)
                break
    return lst

for t in range(1, 11):
    tc = int(input())
    pw = list(map(int, input().split()))


    print(f'#{tc}', end=' ')
    print(*untilzero(pw))

    # goal = pw[-1]
    # print(pw)
    # print(goal)
    # pw.append(pw[0]-1)
    # pw.pop(0)
    # #[9556, 9550, 9553, 9558, 9551, 9551, 9551, 9549]
    #
    # pw.append(pw[0]-2)
    # pw.pop(0)
    # #[9550, 9553, 9558, 9551, 9551, 9551, 9549, 9554]
    #
    # pw.append(pw[0]-3)
    # pw.pop(0)
    # #[9553, 9558, 9551, 9551, 9551, 9549, 9554, 9547]
    #
    # pw.append(pw[0] - 4)
    # pw.pop(0)
    # #[9558, 9551, 9551, 9551, 9549, 9554, 9547, 9549]
    #
    # pw.append(pw[0] - 5)
    # pw.pop(0)
    # #[9551, 9551, 9551, 9549, 9554, 9547, 9549, 9553]
    #
    # # print(pw)
    # # print(goal)

    # for num in pw:
    #     while num > 0:
    #         if pw.count(0) == 1:
    #             break
    #         for i in range(1, 6):
    #             pw.append(pw[0]-i)
    #             pw.pop(0)
    # print(f'#{tc} {pw}')

    #
    # while True: #0 in pw
    #     if pw.count(0) == 1:
    #         break
    #     for i in range(1, 6):
    #         pw.append(pw[0]-i)
    #         pw.pop(0)
    # print(f'#{tc} {pw}')
    #
    # def untilzero(lst):
    #     for num in lst:
    #         while num in lst >= 0:
    #             if lst.count(0) == 1:
    #                 break
    #                 return lst
    #             for i in range(1, 6):
    #                 lst.append(lst[0]-i)
    #                 lst.pop(0)
    #         return lst
