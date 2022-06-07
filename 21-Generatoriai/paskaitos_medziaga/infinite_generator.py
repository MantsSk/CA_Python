def infinite_generator():
    x = 0
    while True:
        yield x
        x += 1

infinite = infinite_generator()

for i in range(int(float('inf'))):
    pass
