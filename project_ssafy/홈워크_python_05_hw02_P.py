# 1.  어떤 자연수 n이 있을 때, d(n)을 n의 각 자릿수 숫자들과 n 자신을 더한 숫자라고 정의하자.       
# 예를 들어 d(91) = 9 + 1 + 91 = 101일 때, n을 d(n)의 제네레이터(generator)라고 한다. 
# 함수 fn_d(n)을 정의하여 보라
def fn_d(n):
    each_sum = 0
    for i in str(n):
        each_sum += int(i)
    return each_sum + n

print(fn_d(91))

#교수님 풀이-------------------------------
def fn_dp(n):
    result = n #와 개천재다 첨부터 n
    while n!= 0:
        result += n % 10 #4, 3, 2, 1
        n = n // 10
    return result
#----------------------------------------

# 2.  어떤 숫자들은 하나 이상의 제네레이터를 가지고 있는데, 101의 제네레이터는 91 뿐 아니라 100도 있다.      
# 반대로, 제네레이터가 없는 숫자들도 있으며, 이런 숫자를 인도의 수학자 Kaprekar가 셀프 넘버(self-number)라 이름 붙였다.
# 예를 들어 1, 3, 5, 7, 9, 20, 31 은 셀프 넘버# 들이다.       
# 셀프넘버를 판별하는 함수 is_selfnumber(n)를 앞서 작성한 fn_d(n) 을 사용하여 작성하라.
def fn_d(n):
    each_sum = 0
    for i in str(n):
        each_sum += int(i)
    return each_sum  + n

def is_selfnumber(n):
    num = n

    while True:
        if fn_d(num) == n:
            print("셀프 아님")
            break
        
        if num == 1: #무한반복을 멈춰줄 조건
            print("셀프임")
            break
        num -= 1
is_selfnumber()

#교수님 풀이----------------------------------
#31의 제네레이터 될 수 있는 목록 : 1-31
#1, 2, 11, 21, .... 전부 fnd에 집어넣기

def is_selfnumber(M):
    #M의 제네레이터가 될 수 있는 경우는
    #1부터 M까지의 숫자중에 있다.
    for i in range(1, M+1):
        #제네레이터인지 아닌지 판별하는 방법은
        #숫자 i를 fn_d에 집어넣었을때 그 값이
        #내가 할당받은 M과 동일하다면,
        #i를 M의 제네레이터라고 할 수 있다.
        if fn_d(i) == M: #fn_d(91) == 101 : 91은 101의 제네레이터
            #하나라도 제네레이터가 있으면?
            #셀프넘버가 아니므로 셀프 넘버를 판별하는 함수
            #is_selfnumber 함수는 False를 반환하고 종료
            return False
    #모든 후보군 모두 출력했는데 False가 반환되지 않았다면
    #셀프 넘버가 맞다
    return True

#람다함수써서 한줄로 만들기
def is_self(M):
    for i in range(1, M+1):
        #lambda [parameter] : expression
        #모든 자리수의 합 + 본인을 더한 값
        #while 나머지를 사용해서 더해왔는데...
        #문자열로 바꿔서 각 자리수를 순회하며 더하기
        #'1234' => '1', '2', '3', '4'
        #[int(char) for char in 'M'] => [1, 2, 3, 4] + [M]
        #=> sum([1, 2, 3, 4, M])
        fn_d = lambda n: sum([int(char) for char in str(n)] + [n])
        if fn_d(i) == M:
            return False
    return True

# def is_selfnumber(M):
#     for i in range(1, M+1):
#         if fn_d(i) == M:
#             return False
#         else: #한번도 false 안나와야 true... 모든 경우의 수 돌려봐야함 중간에 멈추면 안됨
#             return True 