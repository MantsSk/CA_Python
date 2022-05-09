text = ""

sentence_count = int(input("Iveskite sakiniu kieki "))

for sentence in range(0, sentence_count):
    text += input("Įveskite eilutę: ") + "\n"

file_name = input("Įveskite failo pavadinimą: ")

with open(file_name + ".txt", "w", encoding="UTF-8") as write_file:
    write_file.write(text)

with open(file_name + ".txt", "r", encoding="UTF-8") as read_file:
    for sentence in read_file:
        print(sentence, end="")





