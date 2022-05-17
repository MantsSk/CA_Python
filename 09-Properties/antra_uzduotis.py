class Person():

    def __init__(self, firstname, lastname):
        self.first = firstname
        self.last = lastname

    @property
    def fullname(self):
        return self.first + ' '+ self.last

    def email(self):
        return '{}.{}@email.com'.format(self.first.lower(), self.last.lower())
        