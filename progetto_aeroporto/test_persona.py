import unittest
from persona import Persona  
from guardia import Guardia
from passeggero import Passeggero
from capitano import Capitano


class TestPersona(unittest.TestCase):
    def test_creazione_persona(self):
        persona = Persona("Mario", 30)
        self.assertEqual(persona.get_nome(), "Mario")
        self.assertEqual(persona.get_eta(), 30)
        

    def test_creazione_guardia(self):
        guardia = Guardia("Luigi", 40)
        self.assertEqual(guardia.get_nome(), "Luigi")
        self.assertEqual(guardia.get_eta(), 40)
   
    def test_creazione_passeggero(self):
        passeggero = Passeggero("Anna", 30, False, "ABC123")
        self.assertEqual(passeggero.get_nome(),"Anna")
        self.assertEqual(passeggero.get_età(), 30)
        self.assertEqual(passeggero.get_is_something_not_allowed(), False)
        self.assertEqual(passeggero.get_codice_imbarco(), "ABC123")

    def test_creazione_capitano(self):
        capitano = Capitano("Carlo", 45, 20)
        self.assertEqual(capitano.get_nome(), "Carlo")
        self.assertEqual(capitano.get_età(), 45)
        self.assertEqual(capitano.get_esperienza_volo(), 20)
