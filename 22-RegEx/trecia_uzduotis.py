import re

text = '''Workshop & Tutorial proposals: November 21, 2019
Notification of acceptance: December 1, 2019
Workshop & Tutorial websites online: December 18, 2019
Workshop papers: February 28, 2020
Workshop paper notifications: March 27, 2020
Workshop paper camera-ready versions: April 10, 2020
Tutorial material due (online): April 10, 2020'''

pattern = re.compile(r'''
                        (.+)                         # group 1
                        :\s
                        ([A-Z]\w+\s\d{1,2},\s20\d{2}) # group 2
                        ''', re.X | re.M)
# (^.+):\s([A-Z]\w+\s\d{1,2},\s20\d{2})

seq = 1
for line in text.splitlines():
    res = pattern.search(line)
    print(f'{seq}.\nEvent: {res.group(1)}\nDate: {res.group(2)}\n')
    seq += 1
    print(line)


