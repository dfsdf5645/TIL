# start = 0

# while start <= 1000:
    
#     import random
#     numbers = list(range(1,46))

#     x = 0
#     mine = []
#     while x < 6:
#         mine.append(random.choice(numbers))
#         x = x + 1

#     import requests
#     r = requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1049').json()

#     lotto = [r['drwtNo1'],r['drwtNo2'],r['drwtNo3'],r['drwtNo4'],r['drwtNo5'],r['drwtNo6']]

#     k = 0
#     for i in mine:
#         if i in lotto:
#             k = k+1

#     if k == 5:
#         print("3등")
#     elif k == 4:
#         print("4등")
#     elif k == 3:
#         print("5등")
#     else:
#         print("꽝")
#     start = start + 1



# 교수님

import random
# 파이썬으로 웹 요청 보낼수 있는 라이브러리 불러오기
import requests

# (회차 직접 입력)
# num = input()
num = 1049
# 동행복권 로또 당첨 번호 api 사용하기
url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}'

# 입력받은 회차에 해당하는 당첨번호 확인하기 -> 6개 (보너스번호 제외)
response = requests.get(url).json()

# (선택사항) - 보너스 번호 확인하기
numbers = list(range(1, 7))
# print(numbers)

win_num = []
for no in numbers:
    win_num.append(response[f'drwtNo{no}'])
print(win_num)

count_list = {
    '1등': 0,
    '2등': 0,
    '3등': 0,
    '4등': 0,
    '5등': 0,
    '꽝': 0,
}
for _ in range(1000000):
    my_num = random.sample(range(1, 46), 6)
    count = 0
    for num in my_num:
        if num in win_num:
            count = count + 1

    if count == 6:
        count_list['1등'] = count_list['1등'] + 1
        # print('1등')
    elif count == 5 and response['bnusNo'] in my_num:
        count_list['2등'] = count_list['2등'] + 1
    elif count == 5:
        count_list['3등'] = count_list['3등'] + 1
    elif count == 4:
        count_list['4등'] = count_list['4등'] + 1
    elif count == 3:
        count_list['5등'] = count_list['5등'] + 1
    elif count <= 2:
        count_list['꽝'] = count_list['꽝'] + 1

print(count_list)

# 4. 이걸 1000번 반복한다. 
# 1. 로또 번호 6개를 추첨 받는다.
# 2. 내가 추첨 받은 6개의 번호가 1049회차 당첨 번호와 일치 하는지 확인한다.
# my_num = [1, 2, 3, 4, 5, 6]