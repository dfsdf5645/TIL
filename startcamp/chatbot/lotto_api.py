# 파이썬으로 웹 요청 보낼수있는 라이브러리 불러오기
# 동행복권 로또 당첨 번호 api 사용하기 (회차 직접 입력)
# 입력받은 회차에 해당하는 당첨번호 확인하기 -> 6개 (보너스번호 제외)

# 선택사항 - 보너스 번호 확인하기

import requests

name = input("회차를 입력해주세요 : ")
print(name)

# f-string
# f'문자열 {변수}'
r = requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={name}').json()

print('당첨번호는',r['drwtNo1'],r['drwtNo2'],r['drwtNo3'],r['drwtNo4'],r['drwtNo5'],r['drwtNo6'],'입니다.')

list = [r['drwtNo1'],r['drwtNo2'],r['drwtNo3'],r['drwtNo4'],r['drwtNo5'],r['drwtNo6']]
print('당첨번호는',list,'입니다.')

# num = lst(range(1,7))
# int(num)
# for i in num:
#     print(response[f'drwtNo{i}']) >>> 나중에 다시 해보기


x = 0
mine = []
while x < 6:
    mine.append(random.choice(numbers))
    print(mine)
    x = x + 1

import requests
r = requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1049').json()

lotto = [r['drwtNo1'],r['drwtNo2'],r['drwtNo3'],r['drwtNo4'],r['drwtNo5'],r['drwtNo6']]

k = 0
for i in mine:
    if i in lotto:
        k = k+1

if k == 5:
    print("3등")
elif k == 4:
    print("4등")
elif k == 3:
    print("5등")
else:
    print("꽝")

    