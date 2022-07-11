import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset('iris')
sns.countplot(iris['species'])
plt.show()
