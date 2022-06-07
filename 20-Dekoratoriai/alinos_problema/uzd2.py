from time import sleep


def max_args(func):
    def wrapper(*args, **kwargs):
        if len(args) > 4:
            return "too much arguments"
        return func(*args, **kwargs)

    return wrapper


def delay(sec):
    def _delay(func):
        def wrapper(*args, **kwargs):
            sleep(sec)
            print(f"Atidėjimas {sec} sekund.")
            return func(*args, **kwargs)

        return wrapper

    return _delay


@max_args
@delay(3)
def suma(*args):
    return sum(args)


print(suma(2, 3, 4))
