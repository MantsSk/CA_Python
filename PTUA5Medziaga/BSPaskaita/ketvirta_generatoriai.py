def read_in_lines(filename):
    with open(filename, 'r', encoding="utf-8") as file:
        for line in file:
            yield line[:-1]


generator = read_in_lines('tekstas.txt')

for x in generator:
    print(x)

