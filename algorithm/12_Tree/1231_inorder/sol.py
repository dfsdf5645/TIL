import sys
sys.stdin = open('input.txt')

def inorder(node):
    global result
    if node <= N:
        # 왼쪽 자식을 조사
        inorder(2*node)
        result += edge[node][1]
        #오른쪽 자식 조사
        inorder(2*node+1)

for tc in range(1, 11):
    N = int(input())
    edge = [[]] + [list(input().split()) for _ in range(N)]
    result = ''

    inorder(1)
    print(f'#{tc} {result}')