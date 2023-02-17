import sys
sys.stdin = open('sample_input.txt')

def game(start, end):
    if start == end:
        return start
    else:
        center = (start+end)//2
        left = game(start, center)
        right = game(center+1, end)

        if a[left] == a[right]:
            return left
        elif a[left] == 1 and a[right] == 2:
            return right
        elif a[left] == 1 and a[right] == 3:
            return left

        elif a[left] == 2 and a[right] == 1:
            return left
        elif a[left] == 2 and a[right] == 3:
            return right
        elif a[left] == 3 and a[right] == 1:
            return left
        elif a[left] == 3 and a[right] == 2:
            return left

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))
    print(game(0, N-1)+1)
    print(game(a[0],a[-1]))