import datetime

start_time = datetime.datetime.now()
our_range = range(0,100000000)
# x = [1,2,3,4]
y = []

for index in our_range:
    y.append(index)

# for element in x:
#     y.append(element * 2)
 
# print(y)
# print(type(y))
end_time = datetime.datetime.now() - start_time
print("Append in for took: ", end_time)

print("------")

start_time = datetime.datetime.now()

# a = [1,2,3,4]
# b = [element * 2 for element in a]
b = [element for element in our_range]

# print(b)
# print(type(b))
end_time = datetime.datetime.now() - start_time
print("List comprehension took: ", end_time)


