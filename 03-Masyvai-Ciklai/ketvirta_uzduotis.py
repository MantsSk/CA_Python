import copy

my_list = [1,4,5,2,[22,22]]
my_dict = {"Rokas": 18, "Mantas": 25, "Raimonda": 19}

# pirma dalis

# print(my_list[2])
# print(my_dict["Rokas"])

# my_list.append("hey")
# my_dict["Kotryna"] = 22 # arba  my_dict.update({"Kotryna": 22})

# deleted_dict_value = my_dict.pop("Rokas")

# my_list.insert(2, deleted_dict_value)


# ------------- problemos demonstravimas

# new_list = my_list

# new_list[2] = 1000

# print(my_list) 

# ------------ problemos sutvarkymas 

# new_list = my_list[:]

# new_list[2] = 1000

# print(my_list) 

# problemos sutvarkymas su sarasu sarase

new_list = copy.deepcopy(my_list)

new_list[4][0] = 1000

print(my_list) 
