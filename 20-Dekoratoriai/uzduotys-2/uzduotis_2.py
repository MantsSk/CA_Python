def string_args_only(fn):
    def wrapper(*args, **kwargs):
        for i in args:
            if type(i) != str:
                return "All args must be of type string!"
        return fn(*args, **kwargs)
    return wrapper

@string_args_only
def spausdinti_teksta(*args):
    for tekstas in args:
        print(tekstas)

    return 'Grazintas tekstas'

print(spausdinti_teksta('l', 'vienas', 'aaaaa'))