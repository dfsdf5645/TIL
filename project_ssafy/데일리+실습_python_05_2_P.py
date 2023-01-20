import calc

print(calc.ㅋ(2, 3)) # 5
print(calc.sub(2, 3)) # -1
print(calc.mul(2, 3)) # 6
print(calc.div(2, 3)) # 0.6666666666666666

print(calc.div(2, 0)) # 0으로 나눌 수 없습니다.

try:
    print(10/'a')
except ZeroDivisionError:
    print('0으로 나눌 수 없음')
except TypeError:
    print('정수 이외의 값으로 나눌 수 없음')
