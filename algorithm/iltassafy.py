# import math
#balls=[(0,0), (0,0), (0,0) ...] 이런식으로 리스트 속 튜플로 저장돼있다고 치면
# balls = [(0,0), (23, 0)]

angle = 0
power = 0
dx = 0
dy = 0

# while len(balls) <= 5:
#     balls.append((0,0))
# # print(balls)

if balls[1][0] != 0 and balls[1][1] != 0:
    power = 130
    dx = balls[1][0] - balls[0][0]
    dy = balls[1][1] - balls[0][1]
    deg = math.atan2(dy, dx)
    deg = deg * 180 / math.pi
    angle = 90 - deg

#여기 파워 고치기
elif balls[2][0] != 0 and balls[2][1] != 0:
    power = 115
    dx = balls[2][0] - balls[0][0]
    dy = balls[2][1] - balls[0][1]
    deg = math.atan2(dy, dx)
    deg = deg * 180 / math.pi
    angle = 90 - deg

elif balls[3][0] != 0 and balls[3][1] != 0:
    power = 105
    dx = balls[3][0] - balls[0][0]
    dy = balls[3][1] - balls[0][1]
    deg = math.atan2(dy, dx)
    deg = deg * 180 / math.pi
    angle = 90 - deg

elif balls[4][0] != 0 and balls[4][1] != 0:
    power = 115
    dx = balls[4][0] - balls[0][0]
    dy = balls[4][1] - balls[0][1]
    deg = math.atan2(dy, dx)
    deg = deg * 180 / math.pi
    angle = 90 - deg

# print(angle)