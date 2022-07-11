import numpy as np
import pandas as pd

top = pd.read_csv('https://raw.githubusercontent.com/robotautas/kursas/master/Pandas/top50.csv', encoding='ISO-8859-1')
# Kas naudoja konsole, bus patogiau perziureti:
# pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', 150).__enter__()
top.head()
