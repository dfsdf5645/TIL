from itertools import permutations
from itertools import combinations
from pprint import pprint

a = range(1, 12)
b = list(permutations(a, 2)) #개수도 정해줄 수 잇음
for i in b:
    pprint(i)

#조합
c = list(combinations(a, 3))
for i in c:
    print(i)
