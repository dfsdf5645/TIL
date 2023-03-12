import math
# 테이블 크기
table_width = 254
table_height = 127

# 목적구 넘버
number_of_balls = 5

# 공 직경
D = 5.73

# hole
holes = [(0, 0), (130, 0), (260, 0), (0, 130), (130, 130), (260, 130)]

### Stage 1 ###

# 흰 공 좌표
my_ball = (50, 40)

# 목적구 좌표
yellow_ball = (220, 100)

# 목적구과 hole 사이 거리 가장 가까운 걸 채택
b = 260
hole_num = 0
for i in range(6):
    x, y = holes[i][0], holes[i][1]
    dx = abs(x-yellow_ball[0])
    dy = abs(y-yellow_ball[1])
    if b > math.sqrt(dx**2 + dy**2):
        b = math.sqrt(dx**2 + dy**2)

        hole_num = i

print(b, hole_num)

# 흰 공과 hole까지의 거리
a = math.sqrt(((holes[hole_num][0]-my_ball[0])**2)+(holes[hole_num][1]-my_ball[1])**2)
print('a', a)
# 흰 공과 목적구까지의 거리
c = math.sqrt((my_ball[0]-yellow_ball[0])**2+(my_ball[1]-yellow_ball[1])**2)
print('b', b)
print()
# 쳐야하는 방향과 거리 계산
angle_a = math.atan((holes[hole_num][0]-my_ball[0])/(holes[hole_num][1]-my_ball[1]))

angle_c = math.acos((a**2 + b**2 - c**2)/(2*a*b))

print(angle_a)
print(angle_c)
print()

d = math.sqrt((a**2*(math.sin(angle_c)))**2+((b+D)-(a*math.cos(angle_c)))**2)


print(d)