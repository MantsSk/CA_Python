def find_longest_word(filename):
    longest_word = ""
    with open(filename, "r", encoding="UTF-8") as file:
        for line in file:
            word = line.strip()
            if len(word) > len(longest_word):
                longest_word = word
    return longest_word


filename = "CA_PYTHON/uzduotys/uzduotis_2/words.txt"
longest_word = find_longest_word(filename)
print("Longest Word:", longest_word)
print("Length:", len(longest_word))
