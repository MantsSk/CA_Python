def laikrodis():
    i = iter(range(1, 12))
    while True:
        try:
            yield next(i)
        except StopIteration:
            i = iter(range(1, 12))

pass
