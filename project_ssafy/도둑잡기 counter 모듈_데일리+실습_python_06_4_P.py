# 입장 횟수와 퇴장 횟수의 차이가 0이어야 정상이다. 횟수의 차이가 있을 경우 정말 수상
# 입장 횟수와 퇴장 횟수가 같지 않은 사람을 분별하여 출력하라.
# 제약 조건: collection 모듈의 Counter 객체를 활용해야 한다.

entry_record = ['이싸피', '박장고', '조실습', '이싸피', '조실습', '오디비', '임온실', '조실습', '조실습', '이싸피', '안도둑', '임온실', '최이썬', '오디비', '안도둑', '염자바', '박장고', '조실습',
                '최이썬', '조실습', '염자바', '박장고', '임온실', '임온실', '이싸피', '임온실', '오디비', '조실습', '염자바', '임온실', '박장고', '최이썬', '안도둑', '염자바', '임온실', '박장고', '이싸피', '안도둑',
                '임온실', '오디비', '최이썬', '안도둑', '이싸피', '오디비', '안도둑', '이싸피', '박장고', '박장고', '안도둑', '안도둑', '안도둑', '염자바', '최이썬', '오디비', '오디비', '최이썬', '이싸피', '임온실', '안도둑']

exit_record = ['최이썬', '조실습', '이싸피', '안도둑', '임온실', '안도둑', '이싸피', '오디비', '염자바', '박장고', '최이썬', '이싸피', '염자바', '염자바', '박장고', '임온실', '이싸피',
               '박장고', '안도둑', '염자바', '이싸피', '조실습', '조실습', '임온실', '박장고', '이싸피', '조실습', '박장고', '오디비', '안도둑', '조실습', '임온실', '안도둑', '안도둑', '임온실', '조실습', '최이썬', '안도둑', '임온실',
               '염자바', '이싸피', '임온실', '안도둑', '오디비', '안도둑', '오디비', '임온실', '염자바', '임온실', '박장고', '조실습', '이싸피', '최이썬', '최이썬', '오디비', '오디비', '염자바', '오디비', '안도둑', '박장고']

from collections import Counter

#가장 많이 입장한 세 사람
most_entry = ''
for person in Counter(entry_record).most_common(3): #리스트 안 튜플형태
    most_entry += person[0] + ' ' #각 튜플의 첫번째 요소들만 뽑아옴, ' '로 구분
print(f'가장 많이 입장한 세 사람 : {most_entry}')

#입장 퇴장 횟수가 같지 않은 사람
entry = Counter(entry_record) #입장 카운트
exit = Counter(exit_record) #퇴장 카운트

more_entry = entry - exit #퇴장보다 입장이 더 많은 사람
more_exit = exit - entry #입장보다 퇴장이 더 많은 사람

for counter in more_entry:
    print(f'{counter}는 입장과 퇴장횟수가 같지 않음')
for person in more_exit:
    print(f'{person}는 입장과 퇴장횟수가 같지 않음')
    
#교수님
entry_count_dict = {}
for name in entry_record:
    entry_count_dict[name] = entry_count_dict.get(name, 0) + 1
print(entry_count_dict)

print("입장 기록이 가장 많은 top3")
print(*sorted(entry_count_dict.items(),
            key=lambda item : item[1],
            reverse=True
            )[:3])

exit_count_dict = {name: 0 for name in set(exit_record)}
for name in exit_record:
    exit_count_dict[name] += 1
print(exit_count_dict)

for name, count in entry_count_dict.items():
    print(name, count)
    print('='*30)
    print(name, exit_count_dict[name])
    diff = count - exit_count_dict[name]
    if diff > 0 :
        print(f'{name}은 {diff}만큼 더 입장햇음')
    elif diff < 0:
        print(f'{name}은 퇴장 기록이 {-diff}번 더 많음')