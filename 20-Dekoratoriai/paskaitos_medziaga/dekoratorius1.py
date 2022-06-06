def upper_decorator(func):
    def wrapper(*args, **kwargs):
        non_text = [True for arg in args if type(arg) != str]
        if non_text:
            return "Some arguments are not strings"
        some_text = func(*args, **kwargs)
        return some_text.upper()
    return wrapper


@upper_decorator
def returns_concatenated(str2: str, string: str) -> str:
    return string + str2


@upper_decorator
def returns_string(string: str) -> str:
    return string


@upper_decorator
def returns_reversed_string(string: str) -> str:
    return string[::-1]

a = returns_string(string="Vakaris")
b = returns_reversed_string(string="Vakaris")
c = returns_concatenated("diena", string="Laba")
pass
