from aereo import Aereo 

class Aeroporto:
    def __init__(self, nome_aeroporto= "Fiumicino"):
        self.__nome_aeroporto = nome_aeroporto
        self.__lista_aerei = []

    def get_nome_aeroporto(self):
        return self.__nome_aeroporto

    def get_lista_aerei(self):
        return self.__lista_aerei
    
    def ricevi_aereo(self, aereo):
        if isinstance(aereo, Aereo):
            self.__lista_aerei.append(aereo)
            return "Aereo aggiunto con successo."

    def partenza_aereo(self,aereo):
        if isinstance(aereo, Aereo) and aereo in self.__lista_aerei:
            self.__lista_aerei.remove(aereo)
            return "Aereo decollato con successo."
    
    def get_all_aereo(self):
        for aereo in self.__lista_aerei:
            print(aereo.__str__())
    
#aeroporto = Aeroporto()
#aereo = Aereo()
#aeroporto.ricevi_aereo(aereo)
#aeroporto.get_all_aereo()

