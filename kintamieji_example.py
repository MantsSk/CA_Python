import pickle

a = 10
b = 15

with open("kelikintamieji.pkl", "wb") as pickle_out:
    pickle.dump(a, pickle_out)
    pickle.dump(b, pickle_out)

with open("kelikintamieji.pkl", "rb") as pickle_in:
    naujas_a = pickle.load(pickle_in)
    naujas_b = pickle.load(pickle_in)

print(naujas_a)
print(naujas_b)