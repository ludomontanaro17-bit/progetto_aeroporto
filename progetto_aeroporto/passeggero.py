from persona import Persona

class Passeggero(Persona):
    def __init__(self, nome = "Ludovica", età = 25, is_something_not_allowed = False, codice_imbarco = "XYZ789"):
        super().__init__(nome, età)
        self.__is_something_not_allowed = is_something_not_allowed
        self.__codice_imbarco = codice_imbarco
        
    def get_is_something_not_allowed(self):
        return self.__is_something_not_allowed
    
    def set_is_something_not_allowed(self, value):
        self.__is_something_not_allowed = value

    def get_codice_imbarco(self):
        return self.__codice_imbarco

    def __str__(self):
        base = super().__str__()
        return f"Passeggero: {base}, Codice Imbarco: {self.__codice_imbarco}"


#passeggero = Passeggero("Anna", 30, False, "ABC123")   
#print(passeggero.__str__())