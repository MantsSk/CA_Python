import numpy as np

my_array = np.random.randint(0, 100, 64)
reshaped_array = my_array.reshape(8, 8)
reshaped_again = reshaped_array.reshape(2, 4, 8)
python_array = [1, 2, 3, 4, 5, 6, 7]
# Broadcasting
my_array[4:7] = -50

reshaped_again[:, 1:2, 4:]
reshaped_again[:, 1:2]

sample = np.random.randint(1, 10, 25)
sample_matrix = sample.reshape(5, 5)

pass
