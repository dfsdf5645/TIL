N = int(input())


# if N <= 110:
#     print(99)
# elif 110 < N < 1000:
#     a = []
#     count = 100
#     for i in str(N):
#         a.append(i)
#         b = list(map(int, a))
#     first = b[1] - b[0]
#     second = b[2] - b[1]
#     if first == second:
#         count += 1
#     else:
#         count = count
#     print(count)
# else:
#     print(144)

###############
if N <= 110:
    print(99)
elif 110 < N < 1000:
    plus = (N - 111) // 12
    print(100 + plus)
else:
    print(144)