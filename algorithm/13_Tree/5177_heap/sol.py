import sys
sys.stdin = open('sample_input.txt')

def enq(n):
    global last
    last += 1       #완전이진트리에 마지막 정점에 추가
    heap[last] = n  #마지막 정점에 저장
    c = last        #last는 인덱스임
    p = c//2        #왼오 상관없고 그냥 나누기2하면 부모나옴
    while p > 0 and heap[p] > heap[c]:    #부모가 있고, 부모>자식 조건 검사를 위해
        heap[p], heap[c] = heap[c], heap[p]
        c = p       #옮긴자리에서 부모와 비교하기 위해
        p = c//2
    return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    # print(nums)
    heap = [0] * (len(nums)+1)
    # for i in range(N):
    #     heap[i+1] = nums[i]

    # print(heap)
    last = 0

    for num in nums:
        enq(num)

    print(heap)
    # print(heap[N])
    result = 0
    while N >= 1:
        result += heap[N//2]
        N //= 2

    print(f'#{tc} {result}')