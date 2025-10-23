from persona import Persona
from passeggero import Passeggero
import random

class Guardia(Persona):
    def __init__(self, nome = "Piero", età = 50):
        super().__init__(nome,età)
        self.__sospettati = [] 


    def __str__(self):
        base = super().__str__()
        return f"Guardia: {base} con {len(self.__sospettati)} sospettati."

    def aggiungi_sospettati(self, persona, x = random.randint(0,100)):
        if isinstance(persona, Passeggero) and (x == 1 or x == 0 or x == 2):
            self.__sospettati.append(persona)
            return True 
        else: 
            return False

    def controlla_sospettati(self):
        for i in self.__sospettati:
            if i.get_is_something_not_allowed() is True:
                return f"Sospettato {i.get_nome()} è stato arrestato"
        else: 
            None

guardia = Guardia("Luigi", 40)
#print(guardia.__str__())
#passeggero1 = Passeggero()      
#guardia.aggiungi_sospettati(passeggero1)
passeggero2 = Passeggero()
passeggero2.set_is_something_not_allowed(True)
guardia.aggiungi_sospettati(passeggero2,0)
#print(guardia.__str__())
guardia.controlla_sospettati()
