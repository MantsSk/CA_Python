from file1 import calculate_cube as raise_cube
from utils.file2 import PI as pi_constant
from file3 import calculate_square_root as square_root

num = float(input("Enter a number: "))

cube = raise_cube(num)
result = cube * pi_constant
final_result = square_root(result)
print("Cube multiplied by PI, Square root:", final_result)
