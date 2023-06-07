# Using a large sequence with a for loop
# sequence = [i for i in range(10**10)]  # Create a list of 10 billion numbers
# for item in sequence:
#     print(item)


# Using a generator
# def generator_function():
#     for i in range(10**10):  # Generate numbers on-the-fly
#         yield i
#
# generator = generator_function()
# for item in generator:
#     print(item)