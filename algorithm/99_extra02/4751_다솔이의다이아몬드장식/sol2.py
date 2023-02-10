import sys
sys.stdin = open('input.txt')


deco = ['..#..', '.#.#.', '#.D.#', '.#.#.', '..#..']
T = int(input())
for tc in range(1, T + 1):
    s = input()

    for i in range(5):
        for j in range(len(s)):
            if i == 2:
                print('#.' + s[j] + '.', end='')
            else:
                print(deco[i][0:4], end='')
        print(deco[i][4])