from persona import Persona
from personale_di_bordo import PersonaleDiBordo

class Capitano(Persona):
    def __init__(self, nome = "Mario", età = 60, esperienza_volo = 2000):
        super().__init__(nome,età)
        self.__esperienza_volo = esperienza_volo

    def get_esperienza_volo(self):
        return self.__esperienza_volo
    
    def set_esperienza_volo(self, esperienza_volo):
        self.__esperienza_volo = self.__esperienza_volo + esperienza_volo
    
    def __str__(self):
        base = super().__str__()
        return f"Capitano: {base} con Esperienza di Volo: {self.__esperienza_volo} anni"

#capitano = Capitano("Carlo", 45, 20)
#print(capitano.__str__())