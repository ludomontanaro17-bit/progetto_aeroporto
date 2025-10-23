class Persona:
    def __init__(self, nome = 'Ludovica', età = 24):
        self.__nome = nome
        self.__età = età

    def get_nome(self):
        return self.__nome

    def get_età(self):
        return self.__età 

    def __str__(self):
        return f"Nome: {self.__nome}, Età: {self.__età}"
    

#persona = Persona("Ludovica", 24)
#print(persona.__str__())