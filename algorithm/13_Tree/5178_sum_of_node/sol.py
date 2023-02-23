import sys
sys.stdin = open('sample_input.txt')

def make_tree(n):
    while n > 0:
        heap[n] = heap[n*2] + heap[n*2+1]
        # print(heap[n])
        n -= 1


T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())

    heap = [0] * 1001
    for _ in range(M):
        n1, n2 = map(int, input().split())
        heap[n1] = n2
    # print(heap)

    last = 0
    for i in range(1, N+1):
        while heap[i] == 0:
            last = i
            break
    # print(last)

    make_tree(last)
    print(f'#{tc} {heap[L]}')

