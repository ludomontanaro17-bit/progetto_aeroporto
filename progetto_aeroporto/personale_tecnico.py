from persona import Persona
from personale_di_bordo import PersonaleDiBordo

class PersonaleTecnico(PersonaleDiBordo):
    def __init__(self,nome,età):
        super().__init__(nome,età)
       