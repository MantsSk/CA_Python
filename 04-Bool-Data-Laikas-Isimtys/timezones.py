import datetime

x = [1,2]
y = []


start_time = datetime.datetime.now()

for element in x:
    y.append(element * 2)

end_time = datetime.datetime.now() - start_time
print("Append in for took: ", end_time)

print("------")

start_time = datetime.datetime.now()

a = [1,2,3,4]
b = [element * 2 for element in a]

end_time = datetime.datetime.now() - start_time
print("List comprehension took: ", end_time)
