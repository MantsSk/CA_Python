def args_limiter(fn):
    def wrapper(*args, **kwargs):
        if len(args) > 2:
            return "Too many arguments!"
        return fn(*args, **kwargs)
    return wrapper

@args_limiter
def sumuoti(*args):
    rezultatas = 0
    for skaicius in args:
        rezultatas += skaicius
    return rezultatas

print(sumuoti())