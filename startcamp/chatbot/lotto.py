import random
numbers = list(range(1,46)) #45까지 나옴
#range(n,m) = n부터 m-1까지의 숫자 생성

#넘버스가 가진 숫자 중 무작위 값 하나씩 6번 뽑기
#리스트가 가진 값중 무작위 값 뽑는법은?
print(numbers)
#while문 사용

#중복안됨
print(random.sample(numbers,6))

x = 0
lotto = []
while x < 6:
    lotto.append(random.choice(numbers))
    #만약 뽑은 숫자가 이미 들어있다면?
    print(lotto)
    x = x + 1
#중복 안되게끔 > 리스트 안에 넣기

for i in range(5):
    print(random.sample(numbers,6))
    