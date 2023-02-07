import random

with open('output.txt', 'w') as f:
    print(10, file=f)
    for i in range(10):
        N = random.choice(range(1, 10))
        A = []
        print(N, file=f)
        for i in range(N):
            t = random.choice(range(1, 4))
            AB = sorted(random.sample(range(1, 100), 2))
            print(t, *AB, file=f)