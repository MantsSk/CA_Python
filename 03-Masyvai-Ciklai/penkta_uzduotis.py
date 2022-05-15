salaries = {}
salaries[('John', 'Smith')] = 10000
salaries[('John', 'Smithee')] = 11000
salaries[('Kelly', 'Baker')] = 13000
salaries[('Kevin', 'Smith')] = 13000
salaries[('John', 'Baker')] = 13000
salaries[('John', 'Parker')] = 9999
salaries[('Linda', 'Parker')] = 9999

filtered_surnames = set()

# value for  key, value in my_dict.items() if key[0] == "airport"

for key, value in salaries.items():
    name = key[0]
    surname = key[1]
    salary = value
    if len(surname) > 5 and salary > 9000:
        print(f"Employees name is: {name} {surname}, employee earns: {salary}")
        filtered_surnames.add(surname)

for filtered_surname in filtered_surnames:
    print("If you have this surname, you have good salary: " + filtered_surname)
