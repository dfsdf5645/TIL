from collections import deque

a = deque([1, 2, 3])
print(a.popleft())

q1 = deque()
q1.append(100)
q1.append(200)
print(q1.popleft())

###list > 매우 느려짐
q = []
q.append(1)
q.append(2)
print(q.pop(0))
print(q.pop(0)) #0 붙여줘야함

#빠르게
def enqueue(data):
    global rear
    rear += 1
    queue[rear] = data

def dequeue():
    global front
    front += 1
    return queue[front]

queue = [0] * 3
front = -1
rear = -1

rear += 1
queue[rear] = 1
