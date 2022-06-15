import re

def censorhip(text, *keiksmai):
    pattern = re.compile(r'([A-Za-ząčęėįšųūž])([a-ząčęėįšųūž]+)([a-ząčęėįšųūž])')
    for word in keiksmai:
        grouped = pattern.search(word)
        print(grouped.group())
        censored_part = len(grouped.group(2)) * '*'
        censored_word = pattern.sub(f'\g<1>{censored_part}\g<3>', word)
        text = text.replace(word, censored_word)
    print(text)

censorhip('baisūs žodžiai, tokie kaip Kvaraba, žaltys..', 'Kvaraba', 'žaltys')