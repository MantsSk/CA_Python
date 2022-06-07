from typing import Iterable, Callable


def iteruoklis(objektas: Iterable, func: Callable):
    iteratorius = iter(objektas)
    while True:
        try:
            result = next(iteratorius)
        except StopIteration:
            break

        func(result)


broliai = ['jurgis', 'antanas', 'aloyzas', 'martynas']
iteruoklis(broliai, lambda x: print(len(x)))

