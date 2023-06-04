def log_arguments_and_return(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Return value: {result}")
        return result
    return wrapper

@log_arguments_and_return
def multiply(a, b):
    return a * b

print(multiply(2, 3))