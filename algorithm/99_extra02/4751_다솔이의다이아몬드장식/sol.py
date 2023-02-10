import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    word = input()
    for i in range(5):
        for j in range(len(word)*4 + 1):
            if i == 0 or i == 4:
                if (j-2) % 4:
                    print('.', end='')
                else:
                    print('#', end='')
            elif i == 2:
                print('#.' + '.#.'.join(word) + '.#', end='')
                break
            else:
                if j % 2:
                    print('#', end='')
                else:
                    print('.', end='')
        print()

