from functools import wraps
from time import sleep


def uzvelavimas(laikas):
    def uzvelavimas(fn):
        @wraps(fn)
        def wrapper2(*args, **kwargs):
            sleep(laikas)
            print(f"Funkcija buvo atidėta {laikas} sekundę(-es)")
            return fn(*args, **kwargs)

        return wrapper2

    return uzvelavimas


def args_counter(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print("Args number:", len(args))
        return fn(*args, **kwargs)

    return wrapper


@uzvelavimas(1)
@args_counter
def for_sukimas(kartai):
    for x in range(kartai):
        print(x, " ", end="")
    print()


@args_counter
@uzvelavimas(3)
def sumavimas(*args):
    print("Skaičių suma:", sum(args))


dekoratorius = uzvelavimas(1)
wraperis = dekoratorius(for_sukimas)
# wraperis(10_000)

#for_sukimas(1_000)
sumavimas(1, 2, 3, 4)
