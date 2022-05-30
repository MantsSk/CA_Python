my_dict = {'cat': 10, 'dog': 4, 'pig': 2}

animals = {key: True for key, value in my_dict.items() if value > 5}

animals = {}
for key, value in my_dict.items():
    if value > 5:
        animals[key] = True
pass
