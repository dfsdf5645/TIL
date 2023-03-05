import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split()) #학생수, 한 방 최대인원
st = [[0]*7 for _ in range(2)]

for _ in range(N):
    S, Y = map(int, input().split()) #성별, 학년
    st[S][Y] += 1 #첫번째 리스트가 성별0인 여자, 두번째가 성별1인 남자

room = 0
for s in st: #성별 여자, 남자별
    for y in s: #학년별
        if y == 0:
            pass
        elif y % 2 == 1:
            room += y // K + 1
        else:
            room += y // K
print(room)