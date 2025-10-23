import unittest
from aereo import Aereo
from capitano import Capitano
from passeggero import Passeggero
from guardia import Guardia

class testaereo(unittest.TestCase):
    def test_creazione_aereo(self):
        aereo = Aereo("AZ123", 5000, 180)
        self.assertEqual(aereo.get_codice_volo(), "AZ123")
        self.assertequal(aereo._Aereo__numero_ore_volo_per_pilotarlo, 5000)
        self.assertEqual(aereo._Aereo__capienza_max_passeggeri, 180)

    def test_add_capitano(self):
        aereo = Aereo()
        capitano = Capitano()
        self.assertEqual(aereo.add_capitano(capitano), "Capitano aggiunto con successo.")
        self.assertEqual(capitano.get_esperienza_volo(), 2003)
        capitano2 = Capitano()
        self.assertEqual(aereo.add_capitano(capitano2), "Errore: c'è già un capitano a bordo.")
        
    def test_add_capitano_non_qualificato(self):   
        aereo = Aereo()
        capitano3 = Capitano("Giovanni", 50, 500)
        self.assertEqual(aereo.add_capitano(capitano3),"Errore: il capitano non ha abbastanza esperienza di volo.")
        
    def test_get_lista_persone_in_aereo(self):
        aereo = Aereo()    
        capitano = Capitano()
        aereo.add_capitano(capitano)
        self.assertEqual(len(aereo.get_lista_persone_in_aereo(),1))

    def test_get_capitano(self):
        aereo = Aereo()    
        capitano = Capitano()
        self.assertEqual(aereo.get_capitano(), None)
        aereo.add_capitano(capitano)
        self.assertEqual(aereo.get_capitano(), capitano.__str__())

    def test_add_persona(self):
        aereo = Aereo()
        guardia = Guardia("Luigi", 40)
        self.assertEqual(aereo.add_persona(guardia), "Guardia aggiunta con successo.")
        capitano = Capitano()
        self.assertEqual(aereo.add_persona(capitano), "Capitano aggiunto con successo.")
        passeggero = Passeggero()
        self.assertEqual(aereo.add_passeggero(passeggero), True)
        passeggero2 = Passeggero("Marco", 25, False, "WRONGCODE")
        self.assertFalse(aereo.add_persona(passeggero2))

    def test_start_controllo_guardia(self):
        aereo = Aereo()
        passeggero = Passeggero()
        aereo.add_persona(passeggero)
        self.assertEqual(aereo.start_controllo_guardia(), "Errore: non ci sono guardie a bordo.")
        guardia = Guardia()
        aereo.add_persona(guardia)
        self.assertEqual(aereo.start_controllo_guardia(), None)
        passeggero2 = Passeggero("Luca", 28, True, "XYZ789")
        aereo.add_persona(passeggero2)
        self.assertEqual(aereo.start_controllo_guardia(),"Il passeggero {passeggero2.get_nome()} è stato arrestato")        
       