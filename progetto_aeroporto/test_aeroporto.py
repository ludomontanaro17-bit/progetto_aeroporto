import unittest
from aereo import Aereo

class testaereoporto(unittest.TestCase):
    def test_get_nome(self):
        aeroporto = Aeroporto()
        self.assertEqual(aeroporto.get_nome_aeroporto(), "Fiumicino")
    def test_ricevi_aereo(self):
        aeroporto = Aeroporto()
        aereo = Aereo("AZ123", 5000, 180)
        self.assertEqual(aeroporto.ricevi_aereo(aereo), "Aereo aggiunto con successo.")
        self.assertEqual(len(aeroporto.get_lista_aerei()), 1)

    def test_partenza_aereo(self):
        aeroporto = Aeroporto()
        aereo = Aereo("AZ123", 5000, 180)
        aeroporto.ricevi_aereo(aereo)
        self.assertEqual(aeroporto.partenza_aereo(aereo), "Aereo decollato con successo.")
        self.assertEqual(len(aeroporto.get_lista_aerei()), 0)

        