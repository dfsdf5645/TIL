import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    pz = [list(map(int, input().split())) for _ in range(N)]
    print(pz)

# 검색을 통해 알게 되었는데 전치행렬 만들때 list(zip(*행렬)) 하면 되네요
#  닉네임모하지 2022-11-08 15:51 댓글
# 0 0
# @elcarim 저는 0으로 채운 배열미리 만들어놓고 제대로된 배열 값에서 i,j인덱스값 뒤집에서
# 뒤집어진_list[j][i].append(제대로된_list[i][j]) 이런식으로 넣었는데....ㅋㅋ그런 쉬운방법이있다니....
#
#  박우경_0626297 2021-08-12 17:22 댓글
# 5 0
#  row에서 띄어쓰기 없애고 0으로 split하면 1로된 리스트 나오는데 그중에서 연속으로 k개 있는 요소들을 세면 됩니다.
# 세로줄은 이차원 리스트 돌려서 세어 주시고요.