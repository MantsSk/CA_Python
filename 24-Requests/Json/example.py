import json
import pickle


class Cat:
    def __init__(self, legs=4, color="black"):
        self.legs = legs
        self.color = color

murkis = Cat(4, "rainas")

# Sufeilina, nemoka uzkoduoti
#json_text = json.dumps(murkis)
#same_murkis = json.loads(json_text)

pickled_murkis = pickle.dumps(murkis)
unpickled_murkis = pickle.loads(pickled_murkis)

json_text = json.dumps({"Vienas": True, "du": 1.23, "trys": None})
same_murkis = json.loads(json_text)
pass
