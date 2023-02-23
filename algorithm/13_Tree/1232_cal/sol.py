import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)

    for i in range(N):
        arr = input().split()
        if len(arr) == 2:
            n1 = int(arr[0])
            n2 = int(arr[1])
            tree[n1] = n2
        else:
            par = int(arr[0])
            char = arr[1]
            left = int(arr[2])
            right = int(arr[3])
            tree[par] = arr[1]
            if left[par] == 0:
                left[par] =




def inorder(node):
    if node != 0:
        # 왼쪽 자식을 조사
        inorder(left[node])
        print(node, end=' ')
        #오른쪽 자식 조사
        inorder(right[node])

def postorder(node):
    if node != 0:
        # 왼쪽 자식을 조사
        postorder(left[node])
        # 오른쪽 자식 조사
        postorder(right[node])
        print(node, end=' ')


V = int(input())    #노드의 개수
E = V-1             #간선의 개수
edge = list(map(int, input().split()))
print(edge)

#인덱스 쓸거니 노드개수 + 1
#0번 노드는 없음
parent = [0] * (V+1)         #부모의 정보
left = [0] * (V+1)           #왼쪽 자식 정보
right = [0] * (V+1)          #오른쪽 자식 정보

for i in range(E):
    p, c = edge[i*2], edge[i*2+1]
    print(p, c)
    if left[p] == 0:        #아직 왼쪽 자식 없으면
        left[p] = c         #p번의 왼쪽 자식 c
    else:                   #왼쪽에 자식 있으면
        right[p] = c        #오른쪽에 자식정보 넣음
    parent[c] = p

root = 0
for i in range(1, V+1):     #모든 노드 순회
    if parent[i] == 0:      #부모정보 담았는데, 부모가 없으면 루트
        root = i
        break

#조사를 시작 root 노드부터
preorder(root)
print()
inorder(root)
print()
postorder(root)

