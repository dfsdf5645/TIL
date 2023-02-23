# preorder(i)
# if 0<i<=N:
#     print(i)
#     preorder(i*2)
#     preorder(i*2+1)

'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
def preorder(i):
    if i > 0: #존재하는 정점이면 ,, 인덱스 말하는듯
        print(i,end=' ')
        preorder(left[i])
        preorder[right[i]]
    return

V = int(input())
arr=list(map(int, input().split()))
E = V - 1 #간선수
left = [0] * (V+1)  #부모를 인덱스로 왼쪽 자식 저장
right = [0] * (V+1) # " 오른쪽 자식 저장
par = [0] * (V+1)
# child = [[] for _ in range(V+1)] 일케 합쳐서도 ㄱㄴ

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c
    #child[p].append(c)

root = 1
while par[root] != 0: #부모없는 정점 찾을때까지
    root += 1
print(root)

preorder(root)
