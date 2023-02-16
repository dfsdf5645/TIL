# 부분집합으로 최소합 구하는 문제..
# 한줄에 한개씩 열이 몇번인지,, 열이 N만큼 될때까진 조사
# 행에서 값 0번째 썻나안썻나..
# k번째 행에서
import sys
sys.stdin = open('sample_input.txt')
from itertools import permutations
from pprint import pprint

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(arr)

    a = [i for i in range(N)]
    b = list(permutations(a, N))
    print(b)
    # print(b)
    # print([0][0])
    # for tp in b:
    #
    # for i in b:
    #     pprint(i)

    ans = []
    for tp in b:
        result = 0
        for i in range(N):
            result += arr[i][tp[i]]
        ans.append(result)
    print(min(ans))


    # a = []
    # for lst in arr:
    #     a += [*lst]
    # # print(a)
    # b = list(permutations(a, 3))
    # cb = []
    # for i in b:
    #     # pprint(i)
    #     # pprint(sum(i))
    #     cb.append(sum(i))
    # print(cb)
    # print(min(cb))
    #
