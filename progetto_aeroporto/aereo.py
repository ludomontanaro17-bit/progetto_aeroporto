from persona import Persona
from guardia import Guardia 
from capitano import Capitano
from passeggero import Passeggero

class Aereo:
    def __init__(self, codice_volo = "XYZ789", numero_ore_volo_per_pilotarlo = 1000, capienza_max_passeggeri = 150):
        self.__codice_volo = codice_volo
        self.__numero_ore_volo_per_pilotarlo = numero_ore_volo_per_pilotarlo
        self.__capienza_max_passeggeri = capienza_max_passeggeri
        self.__lista_persone_in_aereo = []

    def get_codice_volo(self):
        return self.__codice_volo

    def get_numero_ore_volo_per_pilotarlo(self):
        return self.__numero_ore_volo_per_pilotarlo
    
    def get_capienza_max_passeggeri(self):
        return self.__capienza_max_passeggeri

    def get_lista_persone_in_aereo(self):       
        for i in self.__lista_persone_in_aereo:
            print(i.__str__())
        return self.__lista_persone_in_aereo

    def add_capitano(self, capitano):           
        if isinstance(capitano, Capitano):
            for i in self.__lista_persone_in_aereo:
                if isinstance(i, Capitano):
                    return "Errore: c'è già un capitano a bordo."
                if capitano.get_esperienza_volo() < self.__numero_ore_volo_per_pilotarlo:
                    return "Errore: il capitano non ha abbastanza esperienza di volo."
            self.__lista_persone_in_aereo.append(capitano)
            capitano.set_esperienza_volo(3)
            return "Capitano aggiunto con successo."

    def get_capitano(self):
        for i in self.__lista_persone_in_aereo:
            if isinstance(i, Capitano):
                return i.__str__()
        return None

    

    def add_persona(self, persona):
        if isinstance(persona, Capitano):
            return self.add_capitano(persona)
        if isinstance(persona, Guardia):
            self.__lista_persone_in_aereo.append(persona)
            return "Guardia aggiunta con successo."
        if isinstance(persona, Passeggero):
            num_passeggeri = sum(1 for p in self.__lista_persone_in_aereo if isinstance(p,Passeggero))
            if num_passeggeri < self.__capienza_max_passeggeri and persona.get_codice_imbarco() == self.__codice_volo:
                self.__lista_persone_in_aereo.append(persona)
                return True
            else: 
                return False 

    def start_controllo_guardia(self):
        if not any(isinstance(persona, Guardia) for persona in self.__lista_persone_in_aereo):
            return "Errore: non ci sono guardie a bordo per effettuare il controllo."
        else:
            for persona in self.__lista_persone_in_aereo:
                if isinstance(persona, Passeggero) and persona.get_is_something_not_allowed():
                    return f"Il passeggero {persona.get_nome()} è stato arrestato"
                else: 
                    return None

    def __str__(self):
        return f"Aereo Codice Volo: {self.__codice_volo}, Ore di Volo Richieste: {self.__numero_ore_volo_per_pilotarlo}, Capienza Massima Passeggeri: {self.__capienza_max_passeggeri}"

#aereo = Aereo()
#print(aereo.__str__())