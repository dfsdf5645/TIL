import sys
sys.stdin = open('sample_input.txt')

def make_tree(n):
    #노드번호가 1일때까지 계속 올라가면서 자식 두개 합 채워줌
    while n > 0:
        heap[n] = heap[n*2] + heap[n*2+1]
        # print(heap[n])
        n -= 1

    #while N != L:
        #p = N//2
        #tree[p] += tree[N]
        #N -= 1
    #print(tree)

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())

    heap = [0] * 1001
    for _ in range(M):
        n1, n2 = map(int, input().split())
        heap[n1] = n2
    # print(heap)

    #숫자가 채워져있는곳을 찾아서 그 직전 노드 위치?를 알아냄
    #거기서부터 자식 두개의 합을 그 칸마다 채워주면서 올라감
    last = 0
    for i in range(1, N+1):
        while heap[i] == 0:
            last = i
            break
    # print(last)

    make_tree(last)
    print(f'#{tc} {heap[L]}')

