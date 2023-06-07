def decorator_function(original_function):
    def wrapper_function():
        print("Before the function execution")
        original_function()
        print("After the function execution")
    return wrapper_function

# @decorator_function
def hello():
    print("Hello, world!")

hello()

# hello = decorator_function(hello)
