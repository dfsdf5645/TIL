# import sys
# input = sys.stdin.readline
import sys
sys.stdin = open('input.txt')

def enq(n):
    global last
    last += 1
    heap[last] = n
    c = last
    p = c // 2
    while p > 0 and heap[p] < heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2
    return

N = int(input())
heap = [0] * 20
last = 0

for k in range(N):
    i = int(input())
    if i > 0:
        enq(i)
        print(f'enq {heap}')
    elif i == 0:
        print(heap.pop(1))
        print(f'deq {heap}')

