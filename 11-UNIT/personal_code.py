
class PersonalCode:
    
    def __init__(self, kodas):
        self.__kodas = kodas
    
    def return_last_four(self):
        return str(self.__kodas)[-4:]
    
    def return_first_four(self):
        return str(self.__kodas)[:4]

    @property
    def kodas(self):
        return self.__kodas

    @kodas.setter
    def kodas(self,new_value):
        self.__kodas = new_value
        

