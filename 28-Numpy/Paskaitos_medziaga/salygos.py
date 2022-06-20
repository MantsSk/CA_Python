import numpy as np

my_array = np.random.randint(0, 100, 64)
reshaped_array = my_array.reshape(8, 8)
reshaped_again = reshaped_array.reshape(2, 4, 8)
python_array = [1, 2, 3, 4, 5, 6, 7]

bool_array = reshaped_array > 50
# Pakeicia forma i vienmati
filtered_reshaped = reshaped_array[bool_array]
filtered_reshaped.shape
pass
