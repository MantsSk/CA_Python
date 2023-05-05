numbers = input("Enter a list of numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]
average = sum(numbers) / len(numbers)
print("The average is:", average)
