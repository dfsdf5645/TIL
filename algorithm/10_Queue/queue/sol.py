from collections import deque

a = deque([1,2,3])
# a.append(1)
# a.append(2)
# a.append(3)

a.popleft()

print(a)

a.popleft()
print(a)

a.pop()
print(a)



