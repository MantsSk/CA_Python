import pickle

import pandas as pd

pickled_model = open('deivido_zuvys.pickle', 'rb')
loaded_model = pickle.load(pickled_model)

fish = pd.read_csv(
        'https://raw.githubusercontent.com/robotautas/kursas/master/Machine%20Learning/Fish.csv')
dummies = pd.get_dummies(fish['Species'])
data = pd.concat([fish, dummies], axis=1)
data.drop('Species', axis=1, inplace=True)
X = data[data.columns.drop('Weight')]

loaded_model.predict([X.loc[0]])
