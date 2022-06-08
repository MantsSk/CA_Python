import re

def censorhip(text, *args):
    pattern = re.compile(r'([a-ząčęėįšųūž])([a-ząčęėįšųūž]+)([a-ząčęėįšųūž])')
    for word in args:
        grouped = pattern.search(word)
        censored_part = len(grouped.group(2)) * '*'
        censored_word = pattern.sub(f'\g<1>{censored_part}\g<3>', word)
        text = text.replace(word, censored_word)
    print(text)

censorhip('baisūs žodžiai, tokie kaip kvaraba, žaltys..', 'kvaraba', 'žaltys')