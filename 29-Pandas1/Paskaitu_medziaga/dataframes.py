import numpy as np
import pandas as pd

df = pd.DataFrame(data=np.random.rand(5,6),
                  index=['a', 'b', 'c', 'd', 'e'],
                  columns=['U', 'V', 'W', 'X', 'Y', 'Z'])
df.drop()
