import unittest
from persona import Persona  
from guardia import Guardia
from passeggero import Passeggero

class TestGuardia(unittest.TestCase):
    def test_aggiungi_sospettati(self):
        guardia = Guardia()
        passeggero1 = Passeggero()
        self.assertEqual(guardia.aggiungi_sospettati(passeggero1,1), True)
        passeggero2 = Passeggero()
        self.assertEqual(guardia.aggiungi_sospettati(passeggero2, 4), False)

    def test_controlla_sospettati(self):
        guardia = Guardia()
        passeggero1 = Passeggero()      
        guardia.aggiungi_sospettati(passeggero1,1)
        self.assertEqual(guardia.controlla_sospettati(), None)
        passeggero2 = Passeggero()
        passeggero2.set_is_something_not_allowed(True)
        guardia.aggiungi_sospettati(passeggero2,0)
        self.assertEqual(guardia.controlla_sospettati(), "Sospettato {passeggero2.get_nome()} è stato arrestato")
       