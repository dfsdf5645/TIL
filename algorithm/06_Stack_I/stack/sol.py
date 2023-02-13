#스택 클래스 만들기
class Stack:
    def __init__(self, size):
        self.size = size
        self.items = [None] * size
        self.top = -1

    #값이 비었는지 확인하는 메서드
    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    #값을 추가하는 메서드
    def push(self, item):
        #가득 차지 않았을 때만 추가
        if self.is_full():
            print('스택이 가득 찼어요!!')
        else:
            self.top += 1
            self.items[self.top] = item

    #현재 top 위치에 있는 값 출력
    def peek(self):
        if self.is_empty():
            raise Exception('스택이 비었습니다.')
        else:
            return self.items[self.top]

    #가득 찼는지 확인하는 메서드
    def is_full(self):
        if self.top + 1 == self.size:
            return True
        else:
            return False
    #값을 제거
    def pop(self):
        if self.is_empty():
            pass
        #비어있지 않으면
        else:
            value = self.items[self.top]
            self.top -= 1
            return value

#길이가 5인 스택 생성하기
s1 = Stack(5)
print(s1.items)
print(s1.is_empty())
print('# s1에 값 A를 추가')
#s1에 값 A를 추가
s1.push('A')
print(s1.items)
print(s1.top)
print(s1.peek())
print('# 스택이 비었을때 PEEK은?')
s2 = Stack(5)
print(s2.peek())
print('# s1에 값 B 추가')
s1.push('B')
s1.push('C')
s1.push('D')
s1.push('E')
print(s1.items)
print(s1.top)
print(s1.peek())
print('# s1이 가득찼을때 값을 추가')
s1.push('F')
print('# s1에서 값 하나 제거')
print(s1.pop())
print(s1.items)
print(s1.top)
print(s1.peek())
print('# s1에서 다시 값 추가')
s1.push('가')
print(s1.items)
print(s1.top)
print(s1.peek())