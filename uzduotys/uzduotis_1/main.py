def count_word_frequency(sentence):
    removable_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '0', '=', '+',
                       '[', '{', '}', ']', ';', ':', '\'', '"', '\\', '|', ',', '<', '.', '>',
                       '/', '?']

    # Pakeiciu simbolius i nieka
    for char in removable_chars:
        sentence = sentence.replace(char, '')

    # Visus zodzius pakeiciu i zodzius is mazuju raidziu
    sentence = sentence.lower()

    # Isskaidau teksta i atskirus zodzius
    words = sentence.split()

    # Suskaiciuoju kiek yra skirtingu zodziu ir sudedu i zodyna
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


sentence = input("Enter a sentence: ")
result = count_word_frequency(sentence)
print(result)

# Tai yra! tiesiog* paprastas ;:">tekstas. Tai tai TAI tAi yRA:::\ tiesiog TekStAs, KuRiO žodžius SUskaiČiuosime,,..
