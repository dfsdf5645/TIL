#최대 100개의 key
#최대힙

def enq(n):
    global last
    last += 1       #완전이진트리에 마지막 정점에 추가
    heap[last] = n  #마지막 정점에 저장
    c = last        #last는 인덱스임
    p = c//2        #왼오 상관없고 그냥 나누기2하면 부모나옴
    while p > 0 and heap[p] < heap[c]:    #부모가 있고, 부모>자식 조건 검사를 위해
        heap[p], heap[c] = heap[c], heap[p]
        c = p       #옮긴자리에서 부모와 비교하기 위해
        p = c//2
    return
#최소힙이면 부등호만 바꿔주면됨

def deq():
    global last
    tmp = heap[1]   #루트 임시저장
    heap[1] = heap[last]    #마지막 정점의 값을 루트로 이동
    last -= 1               #마지막 정점 삭제
    p = 1                   #루트를 부모님으로 놓고
    c = p * 2               #왼쪽자식 번호
    while c <= last:        #자식이 하나 이상 있으면
        if c+1 <= last and heap[c] < heap[c+1]: #오른쪽 자식도 있고, 오른쪽자식이 더 큼
            c += 1          #비교대상을 오른쪽 자식으로 변경
        if heap[c] > heap[p]:   #자식이 부모보다 크면
            heap[c], heap[p] = heap[p], heap[c]
            p = c
            c = p * 2       #더 내려갈지말지
        else:
            break
    return tmp               #아까 20 잠깐 꺼내놧으니..

heap = [0] * 101    #완전이진트리니 1-100번 인덱스 준비
last = 0            #완전이진트리의 마지막 정점 번호
#0번 안쓸거지만 일단 last 거기로 설정
enq(14)
print(heap[1])      #루트만 꺼내봄
enq(5)
print(heap[1])
enq(20)
print(heap[1])
enq(8)
print(heap[1])

while last > 1:
    print(deq())