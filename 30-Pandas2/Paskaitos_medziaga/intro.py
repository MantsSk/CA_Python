import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.rand(5,6),
                  ['a', 'b', 'c', 'd', 'e'],
                  ['U', 'V', 'W', 'X', 'Y', 'Z'])
table = df[df>.15]
table.isnull()
bupkiai = table.fillna('bupkis')
bupkiai = bupkiai.replace("bupkis", None)
