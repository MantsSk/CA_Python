from functools import reduce


def calculate_product(numbers):
    product = reduce(lambda x, y: x * y,
                     [num for num in numbers if num % 2 == 0])
    return product


def calculate_squares(numbers):
    squares = [num**2 for num in numbers if num % 2 != 0]
    return squares


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
product = calculate_product(numbers)
squares = calculate_squares(numbers)

print("Product of even numbers:", product)
print("Squares of odd numbers:", squares)
