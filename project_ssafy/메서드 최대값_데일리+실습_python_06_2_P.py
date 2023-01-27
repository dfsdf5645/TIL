grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]

# 작물과 가격이 함께 있는 리스트가 존재할 때, 가장 높은 가격을 가지고 있는 작물의 
# 이름을 출력하라. 단, 작물의 이름을 직접 입력하여 출력하지 않는다

new = []
for tuple in grain_lst:
    new.append(tuple[1])
new.sort()
print(new[-1])

# grain_dict = dict(grain_lst)
# key = list(grain_dict.keys())
# value = list(grain_dict.values())
# max_value = max(value)
# print(value.index(max_value))

# max_idx = value.index(max_value)
# print(key[max_idx])
