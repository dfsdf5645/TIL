import sys
sys.stdin = open('input.txt')

def inorder(node):
    global cnt
    if node != 0:
        # 왼쪽 자식을 조사
        inorder(left[node])
        cnt+=1
        #오른쪽 자식 조사
        inorder(right[node])
    return cnt

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    edge = list(map(int, input().split()))

    parent = [0] * (E+2)  # 부모의 정보
    left = [0] * (E+2)  # 왼쪽 자식 정보
    right = [0] * (E+2)

    for i in range(E):
        p, c = edge[i * 2], edge[i * 2 + 1]
        # print(p, c)
        if left[p] == 0:  # 아직 왼쪽 자식 없으면
            left[p] = c  # p번의 왼쪽 자식 c
        else:  # 왼쪽에 자식 있으면
            right[p] = c  # 오른쪽에 자식정보 넣음
        parent[c] = p

    root = 0
    for i in range(1, E+2):     #모든 노드 순회
        if parent[i] == 0:      #부모정보 담았는데, 부모가 없으면 루트
            root = i
            break

    cnt = 0
    print(f'#{tc} {inorder(N)}')
