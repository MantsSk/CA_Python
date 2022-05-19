class Person():

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def email(self):
        return '{}.{}@email.com'.format(self.name.lower(), self.surname.lower())

    @property
    def fullname(self):
        return self.name + ' '+ self.surname
    
